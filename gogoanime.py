import requests
from multi_m3u8 import Multi_m3u8
from bs4 import BeautifulSoup


class GogoAnime:

    __BASE_URL = 'https://ww3.gogoanime2.org'

    def __init__(self, anime_name=None):
        self.anime_name = anime_name

    def fetch_episodes(self):
        soup = BeautifulSoup(requests.get(f"{self.__BASE_URL}/anime/{self.anime_name}").content)
        return [f"{self.__BASE_URL}{link['href']}" for link in soup.find('ul', {'id': 'episode_related'}).find_all('a')]

    def __download_episode(self, item):
        mm = Multi_m3u8(item)
        mm.start_downloader()
        return mm

    def __create_item(self, url):
        return {
            'episode': url.split('/')[-1],
            'url': url,
            'file': f"{url.split('/watch/')[-1]}.mp4".replace('-', '_').replace('/', '_')
        }

    def download_episodes(self, episode_urls):
        for url in episode_urls:
            soup = BeautifulSoup(requests.get(url).content)
            item = self.__create_item(url)
            item['m3u8'] = f"{self.__BASE_URL}/playlist/{soup.find('iframe')['src'].split('/embed/')[-1]}.m3u8"
            yield self.__download_episode(item)
