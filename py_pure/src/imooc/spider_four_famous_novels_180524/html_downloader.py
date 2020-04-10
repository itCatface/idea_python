import requests


class HtmlDownloader:

    def download(self, url):
        if url is None:
            return None
        else:
            html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
            html.encoding = 'gb2312'  # 解决爬取gb2312的网页中文乱码问题
            return html.text.lower()
