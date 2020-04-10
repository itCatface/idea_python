# coding=utf-8
# /usr/bin/env python

"""
Author: vin
date: 2020/3/24 13:57
"""
import hashlib
import hmac
import json
from urllib import parse


class ParrotSignature(object):

    def __init__(self, imei, sn):
        self.sig_basics_key = "iflyrec@recorder-1024"
        self.sig_key = sn + "_" + imei
        # self.sig_key = "parrot"

    def signature(self, sig_dict):
        if "queryString" in sig_dict:
            if len(sig_dict["queryString"]) > 0:
                sig_dict["queryString"] = self.url_params(sig_dict["queryString"])
        if "bodyString" in sig_dict:
            if len(sig_dict["bodyString"]) > 0:
                sig_dict["bodyString"] = json.dumps(sig_dict["bodyString"])
        print("### Signature dict : {}".format(sig_dict))
        sig_list = []
        for key in sig_dict:
            sig_list.append((key, sig_dict[key]))  # 拼装可转换为url格式的list
        sig_list.sort()  # 排序
        sig_string = parse.urlencode(sig_list)
        print("### Signature string : {}".format(sig_string))
        sig = self.hmac_sha256(sig_string)
        print("### Signature is : {}".format(sig))
        return sig

    @staticmethod
    def url_params(param):
        """
        请求params 格式化
        :param param: dict {"param":123}
        :return: string "param=123"
        """
        if len(param) == 0:
            return param
        else:
            url_params = []
            for key in param:
                url_params.append((key, param[key]))
            url_params = parse.urlencode(url_params)
            url_params = parse.unquote(url_params)
            url_params = parse.unquote(url_params)
            return url_params

    def hmac_sha256(self, value):
        """
        加密算法
        :param value:
        :return:
        """
        # 密钥异或运算
        tempKey = self.sig_basics_key + self.sig_key
        temp = self.sig_key[0]
        tempASCII = ord(temp) + 200
        new_key = []
        for i in range(0, len(tempKey)):
            new_temp = (ord(tempKey[i]) ^ tempASCII) & 255
            new_key.append(chr(new_temp))
        new_key = "".join(new_key)
        # hmac sha256 加密
        message = value.encode('utf-8')
        print(new_key.encode('utf-8'))
        sig = hmac.new(bytes(new_key.encode('utf-8')), message, digestmod=hashlib.sha256).hexdigest()
        return sig


if __name__ == "__main__":
    # sig_params = {'X-Session-Id': '202085017107883102',
    #               'X-Device-Id': '866132040012589',
    #               'X-SN-Id': '311904290050001',
    #               'X-Random': 'm2h1oqry756se3kj',
    #               'X-Device-Type': 'parrot',
    #               'path': '/ParrotRecorderAdaptService/v1/protocalInformations',
    #               'X-UTCTime': 'Tue+24+Mar+2020+13:52:34+GMT',
    #               'X-User-Id': '2082256452589107',
    #               'method': 'GET',
    #               'queryString': "",
    #               'bodyString': {"body01": "abc"}
    #               }
    # request = {'path': '/ParrotRecorderAdaptService/v1/protocalInformations', 'method': 'GET'}
    # ParrotSignature(imei='866132040012589', sn='311904290050001').signature(sig_params)

    sigString = "X-Device-Id=869368040019722&X-Device-Type=parrot&X-Random=3281394a02a8fbf7&X-SN-Id=111908200108721&X-UTCTime=Thu+Apr+02+19%3A21%3A15+GMT%2B08%3A00+2020&method=GET&path=%2FParrotRecorderAdaptService%2Fv1%2FprotocalInformations&queryString="
    sig = ParrotSignature("869368040019722", "P111908200108721").hmac_sha256(sigString)
    print(sig)
