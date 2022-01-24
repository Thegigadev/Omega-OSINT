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
from ..Resources.design import coloring
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

	"""async def search2(self, query: str):

		async with aiohttp.ClientSession() as session:
			async with session.get(f"https://www.facebook.com/public/{query}?_fb_noscript=1") as resp:
				text = await resp.text()
				soup = BeautifulSoup(text, "html.parser")
		print([url.attrs['href'] for url in soup.find_all('a', class_="_32mo", href=True)])"""

	async def search(self, query: str):
		searches = []
		found = await self.google.search(f"site:'https://facebook.com' intitle:'{query}'")
		for i in found:
			searches.append(i)
		found = await self.yandex.search(f"site:'https://facebook.com' intitle:'{query}'")
		for i in found:
			searches.append(i)
		found = await self.duck.search(f"site:'https://facebook.com' intitle:'{query}'")
		for i in found: 
			searches.append(i)
		for search in searches:
			print(f"{coloring.FAIL}  -> Link found: {search}")
###################################################
# Dev Notes #
###################################################
# File made by Shell, revised by Roover.
