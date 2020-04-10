# -collections[python内建的集合模块]
from collections import namedtuple

# 1. namedtuple[创建自定义的tuple对象，方便定义数据类型]
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p, p.x, p.y, isinstance(p, Point), isinstance(p, tuple))

# 2. deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('z')
print(q)
q.popleft()
print(q)

# 3. defaultdict[key不存在时返回默认值,其他与dict完全一样]
from collections import defaultdict

d = defaultdict(lambda: 'N/A')
d['key1'] = 'value1'
d['key2'] = 'value2'
print(d['key2'], d['key3'])

# 4. OrderedDict[迭代时可保持key的顺序，dict的key是无序的]
from collections import OrderedDict

d = dict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4'), ('a', 1), ('b', 2), ('c', 3)])
print("d=>", d, "\nd.keys=>", d.keys())

od = OrderedDict(d)
od['key2'] = 'value0002'
keys = list(od.keys())
print("od=>", od, "\nod.keys=>", keys)

# 5. ChainMap
from collections import ChainMap
import os, argparse

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 6. Counter[dict的子类，简单的计数器，可以统计字符出现的次数]
from collections import Counter

c = Counter()
for ch in 'qwerdfqwer':
    c[ch] = c[ch] + 1

print(c)
