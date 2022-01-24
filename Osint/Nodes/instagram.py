###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from ..Resources.Browsers import *
from ..Resources.design import coloring
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
		searches = []
		found = await self.google.search(f"site:'https://instagram.com' intitle:'{query}'")
		for i in found:
			searches.append(i)
		found = await self.yandex.search(f"site:'https://instagram.com' intitle:'{query}'")
		for i in found:
			searches.append(i)
		found = await self.duck.search(f"site:'https://instagram.com' intitle:'{query}'")
		for i in found: 
			searches.append(i)
		for search in searches:
			print(f"{coloring.FAIL}  -> Link found: {search}")
###################################################
# Dev Notes #
###################################################
# File made by Shell, revised by Roover.
