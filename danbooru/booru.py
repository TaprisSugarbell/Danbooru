import contextlib
import random
import string
import logging
import cloudscraper
from typing import Any
from .exceptions import *
from bs4 import BeautifulSoup
from .__vars__ import __version__
from .types.Danbooru_API import *
from .types.Danbooru_Types import *

# logging.basicConfig(level=logging.WARNING,
#                     handlers=[
#                         logging.StreamHandler()
#                     ])
boorulogs = logging.getLogger("Booru")


def random_key(lenght=5, _string=string.hexdigits):
    return "".join(random.choice(_string) for _ in range(lenght))


def add_to_obj(_da: dict or list, obj: Any = PostInfo):
    if isinstance(_da, list):
        return [add_to_obj(i, obj) for i in _da]
    if "id" in _da.keys():
        _da["_id"] = _da["id"]
        _da.pop("id")
    elif "type" in _da.keys():
        _da["_type"] = _da["type"]
        _da.pop("type")
    return obj(**_da)


class Danbooru:
    def __init__(self, username=None, api_key=None, password=None, host="danbooru", _session=None):
        self.__host = host.lower()
        self.__base = f"https://{self.__host}.donmai.us/"
        self.__sess = _session or cloudscraper.Session()
        self.__session = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            },
            sess=self.__sess
        )
        self.username = username
        _r = self.__session.get(self.__base)
        soup = BeautifulSoup(_r.content, "html.parser")
        self.__authenticity_token = soup.find("meta", attrs=dict(name="csrf-token")).get("content")
        if username and api_key:
            self.__params = dict(login=username, api_key=api_key)
        elif username and password:
            self.__params = {"session[name]": username, "session[password]": password}
        else:
            self.__params = {}
        self.__params.update(dict(authenticity_token=self.__authenticity_token))

    def __set_params(self, **kwargs):
        return self.__params.update(dict(**kwargs))

    def __session_requests(self, url, method="GET"):
        return self.__session.request(method, url, params=self.__params)

    def create_account(self, username: str = None, password: Any = random_key(6), email: Any = None):
        username = self.username or username or random_key(10)
        self.__params.update({"session[name]": username,
                              "session[password]": password,
                              "user[name]": username,
                              "user[email]": email,
                              "user[password]": password,
                              "user[password_confirmation]": password})
        return {
            "username": username,
            "password": password,
            "user": add_to_obj(
                self.__session.post(
                    f'{self.__base}users.json', params=self.__params
                ).json(),
                DanbooruAccount,
            ),
        }

    def update_account(self, **kwargs):
        for k, v in kwargs.items():
            self.__params.update({f"user[{k}]": v})
        _login = self.login()
        self.__session.patch(
            f"{self.__base}users/{str(_login.id)}.json", params=self.__params
        )
        return True

    def login(self):
        if "api_key" in self.__params.keys():
            _da = self.__session.get(
                f"{self.__base}profile.json", params=self.__params
            ).json()
            return DanbooruAccount(*_da.values())
        else:
            # BETA
            _da = self.__session.post(
                f"{self.__base}session.json", params=self.__params
            ).json()
            try:
                return DanbooruAccount(_id=_da["id"],
                                       name=_da["name"],
                                       level=_da["level"],
                                       inviter_id=_da["inviter_id"],
                                       created_at=_da["created_at"],
                                       post_update_count=_da["post_update_count"],
                                       note_update_count=_da["note_update_count"],
                                       post_upload_count=_da["post_upload_count"],
                                       is_banned=_da["is_banned"],
                                       can_approve_posts=_da.get("can_approve_posts"),
                                       can_upload_free=_da.get("can_upload_free"),
                                       level_string=_da["level_string"]
                                       )
            except KeyError as e:
                msj_err = _da.get("message")
                _err = _da.get("error")
                if "AuthenticationFailure" in msj_err:
                    raise DanbooruAuthenticationFailure(msj_err) from e
                elif "RateLimiter" in _err:
                    raise DanbooruLoginRateLimitError(_da["message"]) from e
                else:
                    raise DanbooruUnknownError() from e

    def users(self, user_id: int = None):
        with contextlib.suppress(KeyError):
            user_id = user_id or self.login().id
        if user_id:
            return self.__session.get(f'{self.__base}users/{user_id}.json').json()

    def create_api(self, api_name=None):
        _login = self.login().id
        self.__params.update({
            "api_key[name]": api_name or random_key(),
            "commit": "Create"
        })
        return self.__session.post(
            f"{self.__base}api_keys.json", params=self.__params
        ).json()

    def view_apis(self):
        _login = self.login()
        return self.__session.get(
            f"{self.__base}users/{str(_login.id)}/api_keys.json",
            params=self.__params,
        ).json()

    def view_api(self, api_id: int = None, api_name: str = None):
        _api = None
        _login = self.login()
        _apis = self.view_apis()
        _len_apis = len(_apis)
        print(_len_apis)
        if _len_apis == 0:
            _api = self.create_api()
        elif api_id:
            for _e in _apis:
                if api_id == _e["id"]:
                    _api = _e
                    break
        elif api_name:
            for _e in _apis:
                if api_name == _e["name"]:
                    _api = _e
                    break
        else:
            _api = _apis[-1]
        _r = self.__session.get(
            f"{self.__base}users/{str(_login.id)}/api_keys", params=self.__params
        )
        soup = BeautifulSoup(_r.content, "html.parser")
        # print(soup)
        # _get_api = soup.find("tr", attrs={"data-id": str(_api["id"])})
        # _api_name = _api["name"]
        # _api_key = _get_api.find("td", class_="key-column col-expand").string.strip()
        # _uses = _api["uses"]
        # _last_use = _api["last_used_at"]
        # _created = _get_api.find("td", class_="created-column").find("time").string.strip()
        # return DanbooruAPI(*(_api_name, _api_key, _uses, _last_use, _created))

    def autocomplete(self,
                     query: str = None,
                     _type: str = "tag_query",
                     limit: int = None
                     ) -> list[Autocomplete]:
        _ad = {
            "search[query]": query,
            "search[type]": _type,
            "limit": limit
        }
        self.__params.update(_ad)
        _da = self.__session_requests(f"{self.__base}autocomplete.json").json()
        return add_to_obj(_da, Autocomplete)

    def tags(self,
             name_or_alias_matches: str = None,
             category: Category = None,
             order: str = "date",
             page: int = None,
             limit: int = None,
             hide_empty: str = "yes",
             commit="Search") -> list[Tag]:
        self.__params.update(
            {
                "search[name_or_alias_matches]": name_or_alias_matches,
                "search[order]": order,
                "page": page,
                "limit": limit,
                "search[category]": category,
                "search[hide_empty]": hide_empty,
                "commit": commit
            }
        )
        _da = self.__session_requests(f"{self.__base}tags.json").json()
        return add_to_obj(_da, Tag)

    def favorites(self):
        _login = self.login()
        self.__params.update(dict(user_id=_login.id))
        return self.__session.get(
            f'{self.__base}favorites.json', params=self.__params
        ).json()

    def add_favorite(self, post_id: int = 0):
        self.__params.update(dict(post_id=post_id))
        _da = self.__session.post(
            f'{self.__base}favorites.json', params=self.__params
        ).json()
        if _da["success"]:
            return True
        msj_err = _da["message"]
        if "Access denied" in msj_err:
            raise DanbooruAccessDenied(msj_err)
        else:
            raise DanbooruUnknownError()

    def del_favorite(self, post_id: int = 0):
        self.__session.delete(
            f'{self.__base}favorites/{post_id}.json', params=self.__params
        )
        return True

    def post_random(self, **kwargs) -> PostInfo:
        self.__set_params(**kwargs)
        return add_to_obj(
            self.__session_requests(f'{self.__base}posts/random.json').json()
        )

    def post(self, post_id: int, **kwargs) -> PostInfo:
        self.__set_params(**kwargs)
        _da = self.__session_requests(f"{self.__base}posts/{post_id}.json").json()
        return add_to_obj(_da)

    def show_seq(self, post_id: int, **kwargs) -> PostInfo:
        self.__set_params(**kwargs)
        _da1 = self.__session_requests(f"{self.__base}posts/{post_id}/show_seq")
        _da_split = _da1.url.split("/")[-1]
        # pst_id, _tags = (_ for _ in _da_split.split("?q="))
        pst_id = _da_split.split("?q=")[0]
        _da = self.__session_requests(f'{self.__base}posts/{pst_id}.json').json()
        return add_to_obj(_da)

    def searchs(self, **kwargs) -> list[PostInfo]:
        self.__params.update(**kwargs)
        results = self.__session_requests(f"{self.__base}posts.json").json()
        if isinstance(results, dict):
            try:
                __r = [add_to_obj(results)]
            except TypeError as e:
                boorulogs.error("probably limit tags error")
                _da = add_to_obj(results, DEB)
                raise DanbooruLimitError(_da.message) from e
        else:
            __r = [add_to_obj(i) for i in results]
        return __r

    @staticmethod
    def arm_link(search_json: PostInfo, _type="file_url", abso: tuple = None):
        if isinstance(abso, tuple):
            return search_json, getattr(search_json, _type)
        else:
            return getattr(search_json, _type)

    @staticmethod
    def arm_links(iter_list: list[PostInfo], _type="file_url", abso: tuple = None):
        if isinstance(abso, tuple):
            for i in iter_list:
                yield i, getattr(i, _type)
        else:
            for i in iter_list:
                yield getattr(i, _type)

    @property
    def version(self):
        return __version__

    @property
    def host(self):
        return self.__host

    @property
    def site(self):
        return self.__base


arm_link = Danbooru.arm_link
arm_links = Danbooru.arm_links

