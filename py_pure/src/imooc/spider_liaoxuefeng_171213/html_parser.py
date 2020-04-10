import re
from bs4 import BeautifulSoup

import urllib.parse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        # print('要解析的网页地址为:', page_url)
        # print('要解析的网页内容为:', html_cont)

        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):  # 获取页面中其他词条的URL列表
        new_urls = set()

        # links = soup.find_all('a', href=re.compile(r"wiki"))
        links = soup.find_all('a', class_=re.compile(r'x-wiki-index-item'), href=re.compile(r"wiki"))
        print('links size is:', len(links))
        for link in links:
            new_url = link['href']
            print('new_url is:', new_url)
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 拼接URL
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = {'url': page_url}

        title_node = soup.find('div', class_='x-content').find('h4')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='x-wiki-content x-main-content')
        res_data['summary'] = summary_node.get_text()

        # res_data['top_title'] = soup.find('div', class_='x-content').find('h3').get_text()

        # print(soup.find('div', class_=re.compile(r'x-wiki-content x-main-content')))
        # h4s = soup.find_all('h4')
        # for h4 in h4s:
        #     print(h4.get_text())

        # cont_nodes = soup.find('div', class_='x-wiki-content x-main-content').find_all('p')
        # for cont_node in cont_nodes:
        #     print(cont_node.get_text())


        # res_data['wiki_cont'] = cont_node.get_text()

        return res_data
