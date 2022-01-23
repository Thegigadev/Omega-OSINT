###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import aiohttp
from bs4 import BeautifulSoup
import asyncio
###################################################
class DuckDuck:
    """ Class for DuckDuckGo searches and filtering searches to get URLs
    """
    def __init__(self):
        self.headers={
            'accept': '*/*',
            'origin': 'https://lite.duckduckgo.com',
            'referer': 'https://lite.duckduckgo.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36'
        }
        self.repeat = False
        

    async def search(self, query: str, amount: int = None):
        """This function searches and gets a text output for the specific search.

        Args:
            query (str): The search specified
            amount (int, optional): In the event you want to do more than one search on the specific query, this will output more URL's. Defaults to None.

        Returns:
            string or list (if amount is specified): Returns a response text object which will be used in the filter function to scrape the URL's. In the event you use the amount parameter, this instead outputs a list of response text objects.
        """
        async with aiohttp.ClientSession() as session:
            if amount is None:
                async with session.post(f"https://lite.duckduckgo.com/lite/", headers=self.headers, data={'q': query,'kl': None, 'dt': None }) as resp:
                    text = await resp.text()
                    return text
            else:
                texts = []
                s = 0
                start = 0
                async with session.post(f"https://lite.duckduckgo.com/lite/", headers=self.headers, data={'q': query,'kl': None, 'dt': None }) as resp:
                    text = await resp.text()
                    texts.append(text)
                async with session.post(f"https://lite.duckduckgo.com/lite/", headers=self.headers, data={'q': query,'s': s+30, 'o':'json', 'dc':start+16, 'api':'d.js', 'kl':'wt-wt' }) as resp:
                    text = await resp.text()
                    texts.append(text)
                for i in range(amount):
                    async with session.post(f"https://lite.duckduckgo.com/lite/", headers=self.headers, data={'q': query,'s': s+50, 'o':'json', 'dc':start+50, 'api':'d.js', 'kl':'wt-wt' }) as resp:
                        text = await resp.text()
                        texts.append(text)
                return texts



    async def filter(self, resp: str):
        """Filters a response object so that only URL's for the specific search engine is listed

        Args:
            resp (str): Response text object from search

        Returns:
            list: Returns a list of URLs
        """
        soup = BeautifulSoup(resp, "html.parser")
        return [link.attrs['href'] for link in soup.find_all('a', rel='nofollow', href=True)]

    
# async def main():
#     search = DuckDuck()
#     resp = await search.search("site:'https://replit.com' intext:'selfbot'", 1)
#     urls = []
#     for item in resp:
#         url = await search.filter(item)
#         urls.append(url)
#     for url in urls:
#         for item in url:
#             print(item)

# if __name__ == '__main__':
#     asyncio.run(main())