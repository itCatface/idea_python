# -*- coding:utf-8 -*-
import requests


def trans():
    words = input("请输入一段要翻译的文字：")
    params = {'i': words, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '15867444761376', 'sign': '7c3a043651ded9304837c810ad1be2b8', 'ts': '1586744476137', 'bv': 'bc250de095a39eeec212da07435b6924',
              'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME'}
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url, params=params)
    result = r.json()
    print('原文: %s=>译文: %s || \njson: %s' % (words, '1', result))
    trans()


if __name__ == '__main__':
    trans()
