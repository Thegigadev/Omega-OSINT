import aiohttp
import asyncio
from bs4 import BeautifulSoup


class Shodan:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}

    async def search(self, query: str):
        """Searches shodan for your specific query

        Args:
            query (str): Query specified for search
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.shodan.io/search?query={query}", headers=self.headers) as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, "html.parser")
                urls = []
                for url in soup.find_all('a', class_='title text-dark', href=True):
                    link = f"https://shodan.io{url.attrs['href']}"
                    urls.append(link)
            print(urls)

    async def report(self, query: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.shodan.io/search/report?query={query}", headers=self.headers) as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, "html.parser")
                title = query
                li_tags = soup.body.findAll('strong')
                for item in li_tags:
                    print(item.text)

                
                
                

        




async def main():
    shodan = Shodan()
    test = await shodan.report("Servers")

if __name__ == '__main__':
    asyncio.run(main())