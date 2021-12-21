from urllib.parse import unquote_plus, urlparse
import urllib.request

# url = "https://danbooru.donmai.us/tags?" \
#       "commit=Search&search%5Bhide_empty%5D=yes&search%5Bname_or_alias_matches%5D=1girl&search%5Border%5D=date"
url = "https://danbooru.donmai.us/tags?search%5Bfuzzy_name_matches%5D=iampenguinj&search%5Border%5D=similarity"
unq_url = unquote_plus(url)
url_parse = urlparse(unq_url)
print(url_parse)
for i in url_parse.query.split("&"):
    _i = i.split("=")
    print(f"Key: {_i[0]} Value: {_i[1]}")




