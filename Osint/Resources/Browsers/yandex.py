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
            list: Returns URLs scraped from the search
        """
        async with aiohttp.ClientSession() as session:
            if amount is None:
                async with session.get(f"https://yandex.com/search/?text={query}", headers=self.headers) as resp:
                    text = await resp.text()
                    soup = BeautifulSoup(text, "html.parser")
                    return [link.attrs['href'] for link in soup.find_all('a', class_='Link Link_theme_normal OrganicTitle-Link organic__url link', href=True)]
            else:
                texts = []
                links = []
                for i in range(amount+2):
                    async with session.get(f"https://yandex.com/search/?text={query}&p={i}", headers=self.headers) as resp:
                        text = await resp.text()
                        texts.append(text)
                for text in texts:
                    soup = BeautifulSoup(text, "html.parser")
                    a_tags = soup.find_all('a', class_='Link Link_theme_normal OrganicTitle-Link organic__url link', href=True)
                    for link in a_tags:
                        links.append(link.attrs['href'])
                return links

    async def image_search(self, path: str):
        async with aiohttp.ClientSession() as session:
            with open(path, 'rb')as f:
                image = f.read()
            async with session.post("https://yandex.com/images-apphost/image-download?cbird=37&images_avatars_size=preview&images_avatars_namespace=images-cbir", headers=self.headers, data=image)as resp:
                if resp.status == 200:
                    k = await resp.json()
                    url = k['url']
                    shard = k['image_shard']
                    id = k['image_id']
                    url = url.replace('preview', 'orig')
                    async with session.get(f"https://yandex.com/images/search?rpt=imageview&url={url}&cbir_id={shard}/{id}", headers=self.headers) as resp:
                        text = await resp.text()
                        soup = BeautifulSoup(text, "html.parser")
                        info = [link.attrs['href'] for link in soup.find_all('a', class_='Link Link_theme_outer CbirSites-ItemDomain CbirSites-ItemDomain_withFavicon', href=True)]
                #     async with session.get(f"https://yandex.com/images/search?rpt=imageview&url={url}&cbir_id={shard}/{id}&cbir_page=similar", headers=self.headers)as resp:
                        
                # else:
                #     text = await resp.text()
                #     print(text)
                
###################################################
# Dev Notes #
###################################################
# File made by Shell.


# if __name__ == '__main__':
#     yandex = Yandex()
#     item = asyncio.run(yandex.image_search("/home/shell/Pictures/cat.jpg"))
#     print(item)
