# 1. StringIO[操作str&在内存中读写]
from io import StringIO

f = StringIO()
f.write('hi')
f.write(' ')
f.write('catface')
print('getvalue()获取写入后的str:', f.getvalue())

f = StringIO('test1 \n test2 \n test3')
print(f.readlines())

# 2. BytesIO(操作二进制数据)
from io import BytesIO

f = BytesIO()
f.write('测试'.encode('utf-8'))  # 写入bytes
print(f.getvalue())

# 类似StringIO，可用一个bytes初始化BytesIO，然后像读文件一样读取
f = BytesIO(b'\xe6\xb5\x8b\xe8\xaf\x95')
print(f.read())
