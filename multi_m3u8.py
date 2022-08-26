from multiprocessing import Process
import os


class Multi_m3u8:

    def __init__(self, item):
        self.item = item
        self.parent_dir = '/content/drive/MyDrive/Anime'
        self.download_dir = f"{self.parent_dir}/{item['url'].split('/')[-2].replace('-', '_')}"
        self.log_dir = f'{self.download_dir}/log'
        self.__check_folders([self.download_dir, self.log_dir])

    def __check_folders(self, dirs):
        for dir in dirs:
            if not os.path.isdir(dir):
                os.makedirs(dir)

    def __repr__(self):
        return f"<Multi_m3u8 {self.item}>"

    @staticmethod
    def __multi_download(input_url, output_path, log_path):
        os.system(f'ffmpeg -i {input_url} -codec copy {output_path} 2> {log_path} -n')

    def start_downloader(self):
        self.item['process_name'] = self.item['file'].replace('.mp4', '')
        self.item['log'] = f"{self.log_dir}/{self.item['file'].replace('.mp4', '_log.txt')}"
        self.item['file'] = f"{self.download_dir}/{self.item['file']}"
        self.process = Process(target=self.__multi_download,
                               args=(self.item['m3u8'],
                                     self.item['file'],
                                     self.item['log'],))
        self.process.name = self.item['process_name']
        self.process.start()
