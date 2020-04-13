# 1. StringIO[操作str-字符串是不可变的&在内存中读写]
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

# ---
# 1. 特殊字符和r
print('hello \nworld \t!')
print(r'hello \nworld \t!')

# 2. 内置方法
s = r'hello world!'
# dir()[查看对象的所有属性和方法]
print('dir(s):', dir(s))
# len()[计算对象长度]
print('len(s):', len(s))
# enumerate()[遍历序列的索引及元素]
for i, v in enumerate(s):
    print('i-v', i, v)

# 3. 字符串方法
# capitalize()[将字符串首字母置为大写其余置为小写]
print('"hello World".capitalize():', "hello World".capitalize())
# title()[将每个单词首字母置为大写]
print('s.title():', s.title())
# lower()和upper()
print('s.lower() & s.upper():', s.lower(), '&', s.upper())
# swapcase()[反转大小写]
print('"Hi".swapcase():', "Hi".swapcase())

# 各种判断isnumeric()、isalpha()、isspace()、isalnum()、isdigit()、isdecimal()、islower()、istitle()、isprintable()、isupper()
# count(子串, *, 开始统计位置, 结束统计位置)[统计子串出现次数]
ss = r'aabbccddeeaabbccddeeaabbccddee'
print('ss.count("dd"):', ss.count("dd", 0, 8))
# find(子串, *, 开始统计位置, 结束统计位置)&rfind()[没有时返回-1]
print('ss.find("dd"):', ss.find("dd", 10, 18))

# index(子串, *, 开始统计位置, 结束统计位置)&rindex()[没有时抛异常]
# endswith(子串, *, 开始统计位置, 结束统计位置)&startswith()
# replace(, *, 最多替换个数)
print('ss.replace("aa", "11"):', ss.replace("aa", "11"))

# strip()&lstrip()&rstrip()[清除左右两边指定字符|默认空格]
print('ss.strip("a"):', ss.strip("a"))

# split(, *, 分割次数限制)&rsplit()[通过指定分隔符分割字符串得到list]
print('ss.split("dd", 2):', ss.split("dd", 2))

# 4. join()&os.path.join()
# -join()[将序列的元素按指定字符连接生成新的字符串]
# 1) 对list进行操作
l = ['a', 'b', 'c', 'd', 'e', 'f']
print('" ".join(l):', " ".join(l))
print('"-".join(l):', "-".join(l))
print('":".join(l):', ":".join(l))
# 2) 对tuple进行操作
# t = ('a', 'b', 'c', 'd', 'e', 'f')
t = tuple(l)  # 上面的简写
print('" ".join(t):', " ".join(t))
print('"-".join(t):', "-".join(t))
print('":".join(t):', ":".join(t))
# 3) 对字符串进行操作
s = r'abcdef'
print('" ".join(s):', " ".join(s))
print('"-".join(s):', "-".join(s))
print('":".join(s):', ":".join(s))
# 4) 对dict进行操作
d = {'name': 'ashe', 'age': '17', 'gender': 'girl'}
print('" ".join(d):', " ".join(d))
print('"-".join(d):', "-".join(d))
print('":".join(d):', ":".join(d))

# -os.path.join()
import os

path = os.path.join('d:/', 'catface/', 'temp.txt')
print('path:', path)

# exercise
s = r'《红楼梦》第六十二回 憨湘云醉眠芍药    呆香菱情解石榴裙'
print('s:', s)
