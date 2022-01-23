################################################### # wait im gonna pull dont do anything
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import aiohttp 
import asyncio
###################################################
class pwn:

    async def check(query):
        account = query.replace("@", "%40")
        async with aiohttp.ClientSession() as session:
            x = await session.get(f"https://haveibeenpwned.com/unifiedsearch/{account}", headers={"x-requested-with": "XMLHttprequest", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36"})
            if x.status == 404:
                print("\n   -> Email not found in haveibeenpwned database.")
            elif x.status == 200:
                print(await x.text())
            else:
                print(x.status)
###################################################
