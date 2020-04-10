#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import binascii
import time


# 处理字符串
def add_txt2str_period(txt, s):
    r = []
    for i in range(0, len(s), 2):
        r.append(s[i:i + 2])
    print('\\x' + txt.join(r))


add_txt2str_period(r'\x', '1122334455')


# 显示文件文本内容
def show_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        r = f.read()
        print(path, '-', len(r), '-', r)
        return r


# 显示文件二进制
def show_file_b(path):
    with open(path, 'rb') as f:
        r = f.read()
        print(path, '-', len(r), '-', r)
        return r


# 显示文件二进制
def show_file_b_hex(path):
    with open(path, 'rb') as f:
        r = f.read()
        hex = binascii.b2a_hex(r)
        print(path, '-', len(hex), '-', hex)
        return hex


# 写bytes到文件
def write_byte2file(byte, path):
    with open(path, 'wb') as f:
        f.write(byte)


path_1wav = r'C:\Users\yhwang22\Desktop\1.wav'
path_1b = r'C:\Users\yhwang22\Desktop\1.b'
path_end = r'C:\Users\yhwang22\Desktop\end.wav'
b1_hex = show_file_b_hex(path_1wav)
b1_hex = b1_hex[0:88]
print(b1_hex)
b1_hex = '5249464624b9000057415645666d74201000000001000100803e0000007d0000020010006461746100b90000'
print(b1_hex)
add_txt2str_period(r'\x', b1_hex)
b_h = b'\x52\x49\x46\x46\x24\xb9\x00\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00\x80\x3e\x00\x00\x00\x7d\x00\x00\x02\x00\x10\x00\x64\x61\x74\x61\x00\xb9\x00\x00'

write_byte2file(b_h + show_file_b(path_1b), path_end)
show_file_b(path_end)


# br = b1[0:44] + b2
# write_byte2file(br, r'C:\Users\yhwang22\Desktop\1b.wav')


# r = show_file_b(r'1.wav')
# print(r[0:44])
# b1 = b1 + r
# print(b1)
# show_file_b_hex(r'1.wav')
#
#
# def show_b(desc, path):
#     with open(path, 'rb') as f:
#         return f.read()  # d = binascii.b2a_hex(r)


# b = show_b('1.b:', r'C:\Users\yhwang22\Desktop\temp.txt')
# print('bbbb', b)


# file = r'C:\Users\yhwang22\Desktop\1.wav1'
# with open(file, 'wb') as f:
#     f.write(b)


# 写二进制文件
def copyfile(path1, path2):
    with open(path1, "rb") as f1:
        with open(path2, "wb") as f2:
            while True:
                strb = f1.read(1024)
                if strb == b"":
                    break
                f2.write(strb)


b_h = b'\x52\x49\x46\x46\x24\xb9\x00\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00\x80\x3e\x00\x00\x00\x7d\x00\x00\x02\x00\x10\x00\x64\x61\x74\x61\x00\xb9'
b = b''

# print('b1', b)
# t = show_b('temp.txt', r'C:\Users\yhwang22\Desktop\temp.txt')
# print('t', t)

b_wav_file = r'C:\Users\yhwang22\Desktop\b_wav_file11.wav'
with open(b_wav_file, 'wb') as f:
    f.write(b)

# -
# show_b('源文件bytes', p1)
# time.sleep(1)
# fr = open(p1, 'rb')
# fw = open(p3, 'wb')
# data = fr.read()
# fw.write(data)
# fw.seek(0x00)
# fw.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# fw.flush()
# fw.close()
# fr.close()
# show_b('写文件bytes', p3)

# show_b('源文件bytes', p3)
# time.sleep(1)
# fr = open(p3, 'rb')
# fw = open(p4, 'wb')
# data = fr.read()
# fw.write(data)
# fw.seek(0x00)
# fw.write(h)
# fw.flush()
# fw.close()
# fr.close()
# show_b('写文件bytes', p4)


# show_b('源文件bytes', p3)
# time.sleep(1)
# fr = open(p3, 'rb')
# fw = open(p4, 'wb')
# data = fr.read()
# fw.write(data)
# fw.seek(0x00)
# fw.write(h)
# fw.flush()
# fw.close()
# fr.close()
# show_b('写文件bytes', p4)

print('运行结束...')
