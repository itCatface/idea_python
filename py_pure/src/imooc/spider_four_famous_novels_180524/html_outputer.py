
from bs4 import BeautifulSoup
import os
import time

from src.imooc.spider_four_famous_novels_180524.html_downloader import HtmlDownloader


class HtmlOutputer:

    def __init__(self):
        self._dir = os.getcwd() + '/temp_file_2'

        if not os.path.exists(self._dir):
            os.mkdir(self._dir)

    def collect_novel_content(self, url):
        text = HtmlDownloader().download(url)
        soup = BeautifulSoup(text, 'html.parser')
        title_node = soup.find('a', href='index.htm')

        txt_path = self._dir + '/' + title_node.text + '.txt'
        if not os.path.exists(txt_path):
            open(txt_path, 'w').close()  ### 创建txt文件 ###

        with open(txt_path, 'a', encoding='utf-8') as f:
            time.sleep(2)  # 防止频繁访问

            text = HtmlDownloader().download(url)
            soup = BeautifulSoup(text, 'html.parser')

            title = soup.find('title').text
            content = soup.find('pre').text

            f.write(title + '\r\n')
            f.write(content + '\r\n\r\n')

            print(title)
