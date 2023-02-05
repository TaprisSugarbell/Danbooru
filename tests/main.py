import os
import logging
# from decouple import config
from danbooru import Danbooru, PostInfo
from danbooru.types.Danbooru_Types import *

# https://danbooru.donmai.us/posts/5406792/show_seq?q=underwear&seq=prev

# logging.basicConfig(handlers=[
#     logging.StreamHandler()
# ])
# USERNAME = config("USERNAME_D", default=None)
# PASSWORD = config("PASSWORD", default=None)
# d = Danbooru(USERNAME, password=PASSWORD)
d = Danbooru()
# for compl in d.autocomplete("bds"):
#     print(compl)
# print(
#     d.show_seq(
#         5406792,
#         q="underwear",
#         seq="prev"
#     )
# )
# print(d.create_account())
# _d = d.searchs(md5="")
# d.post()
# print(d.view_api())
# print(d.post_random())
# print(d.tags("hinata*")[0])
# print(d.autocomplete("hinata*")[0])
# _d = d.searchs(tags="1girl", random=True)
# for i in _d:
#     print(i)
# print(d.searchs())
