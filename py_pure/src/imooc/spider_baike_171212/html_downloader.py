# import requests
#
#
# class HtmlDownloader(object):
#     def download(self, url):
#         if url is None:
#             return None
#         req = requests.get(url)
#         if req.status_code != 200:
#             return None
#         return req.text



import urllib
import urllib.parse
import urllib.request


class HtmlDownloader:

    @staticmethod
    def download(url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
