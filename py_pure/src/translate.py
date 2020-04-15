# -*- coding:utf-8 -*-
# !/usr/bin/env python
import argparse

import requests


def trans():
    # 接收-s参数=>是否显示原json
    parser = argparse.ArgumentParser(description='this is description')
    parser.add_argument('-s', action='store_true', default=False, help='show json?')
    args = parser.parse_args()

    words = input("原文 ")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    params = {'i': words, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'lan-select'}
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url, headers=headers, params=params)
    result = r.json()
    print('译文', result['translateResult'][0][0]['tgt'])
    if args.s:
        print('json', result)
    print()
    trans()


if __name__ == '__main__':
    trans()
