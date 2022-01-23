###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from ..Resources.Browsers import *
###################################################
class Instagram:
    """
        Search Instagram for keyword using search engines and dorking.

        Args:

            Query (str): The keyword you wish to search.

    """
    def __init__(self):
        self.google = Google()
        self.yandex = Yandex()
        self.duck = DuckDuck()

    async def search(self, query: str):
        urls = []
        text = await self.google.search(f"site:'https://www.instagram.com' intitle:'{query}'")
        urls.append(await self.google.filter(text))
        text = await self.yandex.search(f"site:'https://www.instagram.com' intitle:'{query}'")
        urls.append(await self.yandex.filter(text))
        text = await self.duck.search(f"site:'https://www.instagram.com' intitle:'{query}'")
        urls.append(await self.duck.filter(text))
        print(urls)
###################################################