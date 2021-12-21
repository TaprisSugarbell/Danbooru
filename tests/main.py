import os
import logging
from decouple import config
from danbooru import Danbooru, PostInfo
from danbooru.types.Danbooru_Types import *

# logging.basicConfig(handlers=[
#     logging.StreamHandler()
# ])
USERNAME = config("USERNAME_D", default=None)
PASSWORD = config("PASSWORD", default=None)
d = Danbooru(USERNAME, password=PASSWORD)
# print(d.create_account())
# _d = d.searchs(md5="")
# d.post()
# print(d.view_api())
# print(d.post_random())
# print(d.tags("a*"))
# print(d.autocomplete("rias"))
# _d = d.searchs(tags="1girl 1boy", random=True)
# for i in _d:
#     print(i)
# print(d.searchs())
