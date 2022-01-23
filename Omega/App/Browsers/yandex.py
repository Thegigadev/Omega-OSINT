import aiohttp
from bs4 import BeautifulSoup
import asyncio


class Yandex:
    """ Class for Yandex searches and filtering searches to get URLs
    """
    def __init__(self):
        self.headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'host': 'yandex.com',
            'referer': 'https://yandex.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36'
        }

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
                async with session.get(f"https://yandex.com/search/?text={query}", headers=self.headers) as resp:
                    text = await resp.text()
                    return text
            else:
                texts = []
                for i in range(amount):
                    async with session.get(f"https://yandex.com/search/?text={query}&p={i}", headers=self.headers) as resp:
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
        return [link.attrs['href'] for link in soup.find_all('a', class_='Link Link_theme_normal OrganicTitle-Link organic__url link', href=True)]


# async def main():
#     search = Yandex()
#     resp = await search.search("site:'https://github.com' intext:'discord'", amount=5)
#     urls = []
#     for lists in resp:
#         item = await search.filter(lists)
#         urls.append(item)

#     for url in urls:
#         for item in url:
#             print(item)

# if __name__ == '__main__':
#     asyncio.run(main())