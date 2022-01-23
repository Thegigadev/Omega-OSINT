###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import aiohttp
from bs4 import BeautifulSoup
import asyncio

class Google:
    """ Class for Google searches and filtering searches to get URLs
    """
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}

    async def search(self, query: str, amount: int=None):
        """This function searches and gets a text output for the specific search.

        Args:
            query (str): The search specified
            amount (int, optional): In the event you want to do more than one search on the specific query, this will output more URL's. Defaults to None.

        Returns:
            string or list (if amount is specified): Returns a response text object which will be used in the filter function to scrape the URL's. In the event you use the amount parameter, this instead outputs a list of response text objects.
        """
        async with aiohttp.ClientSession() as session:
            if amount is None:
                async with session.get(f"https://www.google.com/search?q={query}",headers=self.headers) as resp:
                    soup = BeautifulSoup(text, "html.parser")
                    return [a_tags.find('a', href=True)['href'] for a_tags in soup.find_all('div', class_='yuRUbf')]
            else:
                texts = []
                links = []
                start= 0
                for i in range(amount+2):
                    async with session.get(f"https://www.google.com/search?q={query}&start={start}",headers=self.headers) as resp:
                        text = await resp.text()
                        texts.append(text)
                        start += 10
                for text in texts:
                    soup = BeautifulSoup(text, "html.parser")
                    a_tags = soup.find_all('div', class_='yuRUbf')
                    for link in a_tags:
                        links.append(link.find('a', href=True)['href'])
                return links

    # async def filter(self, resp: str):
    #     """Filters a response object so that only URL's for the specific search engine is listed

    #     Args:
    #         resp (str): Response text object from search

    #     Returns:
    #         list: Returns a list of URLs
    #     """
    #     soup = BeautifulSoup(resp, "html.parser")
    #     return [a_tags.find('a', href=True)['href'] for a_tags in soup.find_all('div', class_='yuRUbf')]

###################################################
# Dev Notes #
###################################################
# async def main():
#     search = Google()
#     resp = await search.search(query="site:'https://replit.com' intext:'selfbot'", amount=2)
#     print(resp)


            

# if __name__ == '__main__':
#     asyncio.run(main())
###################################################
