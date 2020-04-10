from src.imooc.spider_four_famous_novels_180524.html_downloader import HtmlDownloader
from src.imooc.spider_four_famous_novels_180524.html_outputer import HtmlOutputer
from src.imooc.spider_four_famous_novels_180524.url_manager import UrlManager


class SpiderMain:
    def __init__(self):
        self.url_manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.outputer = HtmlOutputer()
        pass

    def craw(self, url):

        # 1. 获取各个小说的index's url
        novel_urls = self.url_manager.get_all_novel_urls(url)
        for novel_url in novel_urls:
            # 2. 获取指定小说对应的各章节url
            chapter_urls = self.url_manager.get_chapter_urls(novel_url)
            for chapter_url in chapter_urls:
                # 3. 输出各章节内容至对应的txt文件里
                self.outputer.collect_novel_content(chapter_url)


if __name__ == '__main__':
    SpiderMain().craw('http://www.purepen.com/index.html')
