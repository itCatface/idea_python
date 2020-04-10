import requests
import urllib
from urllib import request, parse


# class HtmlDownloader(object):
#     def download(self, url):
#         if url is None:
#             return None
#         req = requests.get(url)
#         if req.status_code != 200:
#             return None
#         return req.text


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is None:
            return None

        return requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}).text

# class HtmlDownloader(object):
#
#     @staticmethod
#     def download(url):
#         if url is None:
#             return None
#         response = urllib.request.urlopen(url)
#         if response.getcode() != 200:
#             return None
#         return response.read()
