# Danbooru

[![PyPI](https://img.shields.io/pypi/v/danbooru)](https://pypi.python.org/pypi/danbooru)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/TaprisSugarbell/Danbooru/main/LICENSE)

- Version: **0.0.9**
- License under: **MIT License**

## Dependencies
- Python: >= 3.9.7
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [cloudscraper](https://github.com/venomous/cloudscraper)

## Example of use

### Danbooru

```python
from danbooru import Danbooru
booru = Danbooru() or Danbooru(host="safebooru")
post_random = booru.post_random()
print(post_random.file_url)
```
#### results

- 1
![Saber alter on a moto with a bikini](https://cdn.donmai.us/sample/64/f6/sample-64f6d3fd5b5e58963e2f033953bc7696.jpg "Fate character")
- 2
![Two character of azur lane, version chibi](https://cdn.donmai.us/original/09/ad/09add2352e3e94a9a55506cda9b67115.jpg "Two chibis")

### Login example

1.
````python
from danbooru import Danbooru
booru = Danbooru("YOUR-USERNAME", "YOUR-API_KEY")
print(booru.searchs(tags="loli"))
````

2.
````python
from danbooru import Danbooru
booru = Danbooru("YOUR-USERNAME", "YOUR-PASSWORD")
print(booru.searchs(tags="1girl 1boy"))
````

3.
````python
from danbooru import Danbooru
booru = Danbooru()
account = booru.create_account()
USERNAME = account["username"]
PASSWORD = account["password"]
print(USERNAME, PASSWORD)
print(booru.searchs(tags="long_hair"))
````

