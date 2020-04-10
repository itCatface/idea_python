# -dict


# dict的key必须是不可变对象(list就是可变对象)
# dict：查找、插入快但是占用内存很大[空间换时间][dict的key必须是不可变对象，因为dict根据key来计算value的存储位置(哈希算法)，字符串、整数等可以，list就不能做为dict的key]
def _19_dict():
    info = {'zhangsan': 99, 'lisi': 88, 'wanger': 77}
    print(info)  # {'zhangsan': 99, 'lisi': 88, 'wanger': 77}
    print(info['zhangsan'])  # 99

    # 没有key则创建key
    info['mazi'] = 66
    print(info)  # {'zhangsan': 99, 'lisi': 88, 'wanger': 77, 'mazi': 66}

    # key已存在则冲掉之前的值
    info['mazi'] = 100
    print(info)  # {'zhangsan': 99, 'lisi': 88, 'wanger': 77, 'mazi': 100}

    # 判断dict中是否存在指定的key
    print(('tt' in info))  # False

    # key不存在返回None
    score = info.get('zhang')
    print(score)  # None

    # key不存在返回None或指定的默认值[如此处的-1]
    score = info.get('zhangsan', -1)
    print(score)  # 99 如果该key不存在则返回-1

    # 删除指定key-value对
    info.pop('mazi')
    print(info)  # {'zhangsan': 99, 'lisi': 88, 'wanger': 77}

    # python基础教程补充如下

    # 1. clear() --> {}

    # 2. copy() --> 得到dict副本

    # 3. fromkeys()
    d = {}.fromkeys(['name', 'age'])
    print(d)  # {'name': None, 'age': None}

    # 4. get(key, defaultValue)

    # 5. has_key() --> 是否含有该键

    # 6. items --> 以列表方式返回{(k1, v1), (k2, v2)...}

    # 7. iteritems() --> iterator

    # 8. keys() & iterkeys()

    # 9. pop(key)

    # 10. popitem() --> 弹出随机键值

    # 11. setdefault() --> 类似get，但可在dict无该key时添加该k-v

    # 12. update() --> 将新dict添加至旧dicr，若有相同key则覆盖

    # 13. values --> 以列表形式返回所有值 & itervalues()


# -set
# key不重复，需要提供一个list作为输入集合[同dict的key不可放入不可变对象]
def _20_set():
    names = ['zhangsan', 1, 2, 'lisi', 1]
    s = set(names)
    print(s)  # {1, 2, 'lisi', 'zhangsan'}    | 无序、自动过滤重复元素

    # add()添加元素，且重复添加无效果
    s.add('wanger')
    # 重复添加不会有效果
    s.add('wanger')
    print(s)  # {1, 2, 'zhangsan', 'lisi', 'wanger'}

    s.remove('wanger')
    print(s)  # {1, 2, 'lisi', 'zhangsan'}


# set和数学上的集合类似
def _21_set():
    l = [1, 2, 3, 4, 5]
    s1 = set(l)  # 通过set()传入list构建一个set集合
    s2 = {2, 3, 4, 5, 6}  # 直接复制一个set集合
    print(s1 & s2)  # {2, 3, 4, 5}
    print(s1 | s2)  # {1, 2, 3, 4, 5, 6}
    print(s1 ^ s2)  # {1, 6}


def _22_sort():
    chars = ['b', 'd', 'a', 'c']
    chars.sort()
    print(chars)  # ['a', 'b', 'c', 'd']

    s = 'abc'
    # replace()创建了一个新字符串'Abc'并返回
    s1 = s.replace('a', 'A')
    print('s1=>', s1, ' || s=>', s)  # s1=> Abc  || s=> abc


# 总结[list&dict(空间换时间)]
# [dict]查找和插入的速度块，不会随着key的增加而变慢
# [dict]占用内存大，浪费内存资源多
# [list]查找和插入的时间随元素的增加而增加
# [list]占用空间小，不浪费内存


# 对于不可变对象，调用自身的任意方法，也不会改变该对象自身的内容。但这些方法会创建新的对象并返回，故保证了不可变对象本身永远是不可变的


_19_dict()
_20_set()
_21_set()
_22_sort()
