import time, os
from datetime import datetime


def encrypt1(var, key):
    encrypted = [chr(ord(a) ^ ord(b)) for (a, b) in zip(var, key)]
    return encrypted

    # return bytes(a ^ b for a, b in zip(var, key))


def open_img(path):
    des_path = 'd:\\t\\%s%s' % (datetime.now().timestamp().__str__().replace('.', '-'), '.jpg')
    print(des_path)

    des_file = open(des_path, 'w')
    des_file.close()

    f = open(des_path, 'a', encoding='utf-8')

    with open(path, 'rb') as f1:
        print(f1.read())

    # for byte in bytes:
    #     pass
        # f.write(str(byte ^ 0X99))

        # print(byte)
        # print(byte ^ 0X99)

        # encrypt1(byte, 0X99)

    # print(encrypt1(open(path, 'r'), 0X99))


open_img('d:\\t\\l.jpg')
