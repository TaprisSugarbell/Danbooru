import danbooru
from setuptools import setup, find_packages


setup(
    name='danbooru',
    version=danbooru.__version__,
    packages=find_packages(),
    url='https://github.com/TaprisSugarbell/Danbooru',
    author='SayuOgiwara',
    author_email='anonesayu@gmail.com',
    description='Unofficial https://danbooru.donmai.us Package',
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4",
        "cloudscraper"
    ]
)
