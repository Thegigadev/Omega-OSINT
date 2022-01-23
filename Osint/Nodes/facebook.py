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
    """
        Search Facebook for keyword using search engines and dorking.

        Args:

            Query (str): The keyword you wish to search.

    """
    def __init__(self):
        self.google = Google()
        self.yandex = Yandex()
        self.duck = DuckDuck()

    async def search_account(self, query: str):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.facebook.com/public/{query}?_fb_noscript=1") as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, "html.parser")
        print([url.attrs['href'] for url in soup.find_all('a', class_="_32mo", href=True)])

    async def search(self, query: str):
        """Search using search engines, uses dorking

        Args:
            query (str): The name/account you want to search

        Returns:
            list: Returns urls in list of lists
        """
        urls = []
        searches = await asyncio.gather(self.google.search(f"site:'https://www.facebook.com' intitle:'{query}'"), self.yandex.search(f"site:'https://www.facebook.com' intitle:'{query}'"), self.duck.search(f"site:'https://www.facebook.com' intitle:'{query}'"))
        print(searches)
        # text = await self.google.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        # urls.append(text)
        # text = await self.yandex.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        # urls.append(text)
        # text = await self.duck.search(f"site:'https://www.facebook.com' intitle:'{query}'")
        # urls.append(text)
        print(urls)
###################################################