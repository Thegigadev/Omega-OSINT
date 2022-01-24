###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
from ..Resources.design import coloring
import aiohttp
import json
###################################################
class pwn:
	"""
		Search HaveIBeenPwned database for email to find if it's been pwned!

		Args:

			Query (str): The email you wish to search.

	"""
	
	async def check(query):
		account = query.replace("@", "%40")
		async with aiohttp.ClientSession() as session:
			z = await session.get(f"https://haveibeenpwned.com/", headers={"x-requested-with": "XMLHttprequest", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36"})
			cookie = z.headers['set-cookie']
			x = await session.get(f"https://haveibeenpwned.com/unifiedsearch/{account}", headers={f"cookie":cookie, "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36", "connection":"keep-alive", "Host":"haveibeenpwned.com", "referer":"https://haveibeenpwned.com"}) 
			if x.status == 404:
				print(f"{coloring.WHITE}  -> Email not found in haveibeenpwned database.")
			elif x.status == 200:
				z = await x.json()
				for name in z['Breaches']:
					print(f"{coloring.FAIL}  -> Breach found: {name['Name']}")
###################################################
# Dev Notes #
###################################################
# File made by Roover and Shell,
