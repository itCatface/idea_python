class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取URL列表
        self.old_urls = set()  # 爬取过的URL列表

    def add_new_url(self, url):  # 添加一个新的URL到待爬取URL列表中
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  # 批量添加URL至待爬取URL列表中
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 是否有待爬取URL
        return len(self.new_urls) != 0

    def get_new_url(self):  # 从待爬取URL列表中获取一个新的URl
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
