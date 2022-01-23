###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from ..Resources.Browsers import *
###################################################
class Twitter:
    """
        Search Twitter for keyword using search engines and dorking.

        Args:

            Query (str): The keyword you wish to search.

    """
    def __init__(self):
        self.google = Google()
        self.yandex = Yandex()
        self.duck = DuckDuck()

    async def search(self, query: str):
        urls = []
        text = await self.google.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(text)
        text = await self.yandex.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(text)
        text = await self.duck.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(text)
        print(urls)
###################################################