# -迭代
from collections.abc import Iterable

print(isinstance('abc', Iterable))  # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance({'name': 'catface'}, Iterable))  # True
print(isinstance(123, Iterable))  # False

l = [1, 'a', True, None]
d = {'a': 1, 'b': 2, 'c': 3}
for v in l:
    print(v)
for key in d:
    print(key, d[key])  # a 1 \n b 2...
for value in d.values():
    print(value)  # 1 2...
for s in 'abcd':
    print(s)  # a b...

# 类似java的索引和值
s = 'abcd'
for i, value in enumerate(s):
    print('s=>', i, value)  # 0 a \n 1 b...

for index, key in enumerate(d):
    print('d=>', index, key)  # 0 a \n 1 b...
    print('d=>', key, d[key])  # a 1 \n b 2...

# 同时引用两个变量
for i, value in [(1, 1), (2, 2), (3, 3)]:
    print(i, value)  # 1 1 \n 2 2...
