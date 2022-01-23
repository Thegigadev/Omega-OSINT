from bs4 import BeautifulSoup
import aiohttp
import asyncio
from .Browsers import *


class Twitter:
    def __init__(self):
        self.google = Google()
        self.yandex = Yandex()
        self.duck = DuckDuck()

    async def search(self, query: str):
        """Search using search engines, uses dorking

		Args:
			query (str): The name/account you want to search

		Returns:
			list: Returns urls in list of lists
		"""
        urls = []
        text = await self.google.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(await self.google.filter(text))
        text = await self.yandex.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(await self.yandex.filter(text))
        text = await self.duck.search(f"site:'https://twitter.com' intitle:'{query}'")
        urls.append(await self.duck.filter(text))
        return urls