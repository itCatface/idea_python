from itertools import islice, cycle


def fn_XOR(txt, key):
    key = bytes(key, 'ascii')
    return (a ^ b for a, b in zip(islice(cycle(key), len(txt)), txt))


def crypt(txt, key):
    return ','.join(map(str, fn_XOR(bytes(txt, 'ascii'), key)))


def decry(txt, key):
    txt = bytes(map(int, txt.split(',')))
    return bytes(fn_XOR(txt, key)).decode()


def encrypt1(var, key):
    # encrypted = [chr(ord(a) ^ ord(b)) for (a, b) in zip(var, key)]
    # return encrypted

    return bytes(a ^ b for a, b in zip(var, key))


if __name__ == '__main__':
    print(encrypt1(b"daniel King ", b"we"))

    # while 1:
    #     flg = int(input('加密 0\n解密 1\n>'))
    #     if flg in (0, 1):
    #         break
    #
    # txt = input('输入%s文内容：' % '明密'[flg])
    # key = input('输入密码：')
    # print('%s文：%s' % ('密明'[flg], decry(txt, key) if flg else crypt(txt, key)))
