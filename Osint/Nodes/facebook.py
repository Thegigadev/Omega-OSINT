###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import sys
from ..Resources.Browsers import *
import asyncio
import aiohttp
from bs4 import BeautifulSoup
###################################################
class Facebook:
    def __init__(self):
        self.google = Google()
        self.yandex = Yandex()
        self.duck = DuckDuck()

    async def search_account(self, query: str):
        """Searches using facebooks requests to find accounts

        Args:
            query (str): Your search query, mostly someones name

        Returns:
            string: A response text object used in filter function  
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.facebook.com/public/{query}?_fb_noscript=1") as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, "html.parser")
        return [url.attrs['href'] for url in soup.find_all('a', class_="_32mo", href=True)]

    # async def filter(self, resp: str):
    #     soup = BeautifulSoup(resp, "html.parser")
    #     return [url.attrs['href'] for url in soup.find_all('a', class_="_32mo", href=True)]

    async def search(self, query: str):
        """Search using search engines, uses dorking

        Args:
            query (str): The name/account you want to search

        Returns:
            list: Returns urls in list of lists
        """
        urls = []
        text = await self.google.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        urls.append(await self.google.filter(text))
        text = await self.yandex.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        urls.append(await self.yandex.filter(text))
        text = await self.duck.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        urls.append(await self.duck.filter(text))
        print(urls)
###################################################