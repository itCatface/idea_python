# f = open('d:\\t\\l.jpg', 'rb')
# f1 = f.read()
# print(f1)
#
#
# hex = f1.encode('hex')
# print(hex)


# def read_bigFile():
#     f = open('d:\\t\\l.jpg', 'rb')
#     cont = f.read()
#     while len(cont) > 0:
#         print(cont)
#         cont = f.read()
#     f.close()
#
#
# read_bigFile()


# filename = 'd:\\t\\l.jpg'
# f = open(filename, 'rb')
# f.seek(0, 0)
# index = 0
# for i in range(0, 16):
#     print("%3s" % hex(i))
#
# for i in range(0, 16):
#     print("%-3s" % "#")
#
# while True:
#     temp = f.read(1)
#     if len(temp) == 0:
#         break
#     else:
#         print("%3s" % temp.encode('hex'))
#         index = index + 1
#     if index == 16:
#         index = 0
#         print()
# f.close()


# import binascii
#
# fh = open(r'd:\\t\\l.jpg', 'rb')
# a = fh.read()
# # print 'raw: ',`a`,type(a)
# hexstr = binascii.b2a_hex(a)  # 得到一个16进制的数
# # print('hex: ', hexstr, type(hexstr))
# bsstr = bin(int(hexstr, 16))[2:]
# print('bin: ', bsstr, type(bsstr))


f = open(r'd:\t\l.jpg', "rb+")
data = f.read()  # 这样data是一个b开头的ASCII数字。
for d in data:
    print(ord(str(d)))

# f.close()
# print(ord(data))  # 将二进制数据转化为10进制数据。
