# -列表生成式[List Comprehensions] --> 创建list的生成式(快速生成list)
l = list(range(2, 9))
print(l)  # [2, 3, 4, 5, 6, 7, 8]

# 列表生成式：要生成的元素 + for (+ if)
l = [x * x for x in range(1, 5)]
print(l)  # [1, 4, 9, 16]

l = [x * x for x in range(2, 6) if x % 2 == 0]
print(l)  # [4, 16]

# 两层循环生成成全排列
l = [x + y for x in range(1, 4) for y in range(5, 11)]
print(l)  # [6, 7, 8, 9, 10, 11, 7, 8, 9, 10, 11, 12, 8, 9, 10, 11, 12, 13]
l = [x + y for x in range(1, 4) if x % 2 == 0 for y in range(5, 11) if y % 2 == 0]
print(l)  # [8, 10, 12]
l = [x + y for x in 'abc' for y in 'xyz']
print(l)  # ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
l = [x + y + z for x in 'ab' for y in 'pq' for z in 'yv']
print(l)  # ['apy', 'apv', 'aqy', 'aqv', 'bpy', 'bpv', 'bqy', 'bqv']

import os

# 列举当前目录所有文件和目录名
l = [d for d in os.listdir('./')]
print(l)  # ['1_section.py', '2_iteration.py', '3_list_creator.py', '4_generator.py', '5_iterator.py']

# 使用两个变量生成list
d = {'name': 'catface', 'age': '27', 'sex': 'male'}
l = [k + '=' + v for k, v in d.items()]
print(l)  # ['name=catface', 'age=27', 'sex=male']

# 练手
l = [x.lower() for x in ['Q', 'W', 'E', 'R', 'd', 'F']]
print(l)  # ['q', 'w', 'e', 'r', 'd', 'f']

l = ['Hello', 'World', 18, 'Apple', None]
l = [x.lower() for x in l if isinstance(x, str)]
print(l)  # ['hello', 'world', 'apple']
