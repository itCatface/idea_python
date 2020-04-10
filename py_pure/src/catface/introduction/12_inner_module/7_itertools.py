# -itertools[提供操作迭代对象的函数]
import itertools

# 无线迭代器count、cycle、repeat，可使用takewhile等函数根据条件截取有限序列
naturals = itertools.count(1)
for n in naturals:
    if n > 7:
        break
    print(n)

cs = itertools.cycle('cat')
for i, c in enumerate(cs):
    if i > 3:
        break
    print(c)

re = itertools.repeat('cat', 3)
for r in re:
    print(r)

naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 7, naturals)
print('ns=>', list(ns))

# chain将一组迭代对象串联
for c in itertools.chain('abc', '123'):
    print(c)

# groupby将迭代器中相邻重复元素挑出来放一起
for k, g in itertools.groupby('aabbcC'):
    print(k, list(g))

for k, g in itertools.groupby('eeffgG', lambda c: c.upper()):
    print(k, list(g))
