# 现在网址已经变成http://baike.baidu.com/item/Python，我们抓这个新网址需要修改成这句links = soup.find_all('a', href=re.compile(r"/item/(.*)"))

import time

from src.imooc.spider_liaoxuefeng_171213 import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # 网页下载器
        self.parser = html_parser.HtmlParser()  # 网页解析器
        self.outputer = html_outputer.HtmlOutputer()  # 爬取内容输出器[输出爬取到的价值信息]

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 有新的URl
            # try:
            new_url = self.urls.get_new_url()  # 爬取这个新的URL
            print("正在爬第:%s个，地址为:%s" % (count, new_url))
            html_cont = self.downloader.download(new_url)  # 下载网页
            new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析网页
            self.urls.add_new_urls(new_urls)  # 将爬取完数据的URL防到已爬取URL集合
            self.outputer.collect_data(new_data)  # 收集爬取到的数据

            if 5 == count:
                break

            count += 1

            time.sleep(3)
            # except:
            #     print("当前地址爬取异常...")

        self.outputer.output_html()  # 将爬取到的数据写到本地


def main():
    root_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    root_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000'
    root_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    # root_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


if __name__ == '__main__':
    main()
