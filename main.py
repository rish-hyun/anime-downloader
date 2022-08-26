from gogoanime import GogoAnime
# from multi_m3u8 import Multi_m3u8

if __name__ == '__main__':

    gg = GogoAnime('shingeki-no-kyojin')
    eps_urls = gg.fetch_episodes()
    ep_data = [res for res in gg.download_episodes(eps_urls)]
