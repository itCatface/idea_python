from bs4 import BeautifulSoup

import re

from src.imooc.spider_four_famous_novels_180524.html_downloader import HtmlDownloader


class UrlManager(object):

    # 获取各个小说的index's url
    def get_all_novel_urls(self, url):
        novel_urls = []

        html = HtmlDownloader().download(url)
        soup = BeautifulSoup(html, 'html.parser')
        novel_nodes = soup.find_all('a', href=re.compile(r"(.*)/index.htm"))
        for novel in novel_nodes:
            novel_urls.append('http://www.purepen.com/' + novel['href'])

        return novel_urls

    # 获取指定小说对应的各章节url
    def get_chapter_urls(self, url):
        chapter_urls = []

        text = HtmlDownloader().download(url)
        soup = BeautifulSoup(text, 'html.parser')

        title_node = soup.find('title').text
        chapter_nodes = soup.find_all('a', href=re.compile(r"(\d).htm"))
        for chapter in chapter_nodes:
            chapter_urls.append(url.replace('index.htm', chapter['href']))

        return chapter_urls
