# -list
def test_list():
    # list是可变、有序集合，且元素不必是同一类型，可随时添加和删除元素
    info = []  # 空的list
    print('info:', info, " | info's length:", len(info))  # info: []  | info's length: 0

    info = ['zhangsan', 'lisi', 19, 57.46, True, None]
    print(info)  # ['zhangsan', 'lisi', 19, 57.46, True, None]

    print(info[4])  # True
    # 最后一个索引可用-1表示
    print(info[-2])  # True

    print(len(info))  # 6

    info.append('extra')
    print(info)  # ['zhangsan', 'lisi', 19, 57.46, True, None, 'extra']

    # 在指定索引处插入元素
    info.insert(1, 'add to index 1')
    print(info)  # ['zhangsan', 'add to index 1', 'lisi', 19, 57.46, True, None, 'extra']

    # 删除最后一个元素
    print(info.pop())
    print(info)  # ['zhangsan', 'add to index 1', 'lisi', 19, 57.46, True, None]

    # 删除指定位置的元素
    # pop()删除并返回该元素值
    info.pop(1)  # extra
    print(info)  # ['zhangsan', 'lisi', 19, 57.46, True, None]

    # 修改指定索引的值
    info[0] = 'first blood'
    print(info)  # ['first blood', 'lisi', 19, 57.46, True, None]

    # 多维list
    info.insert(-1, [3, 2, 'str1'])
    print(info)  # ['first blood', 'lisi', 19, 57.46, True, [3, 2, 'str1'], None]
    print(len(info))  # 7

    # 同上删除元素
    del info[3]
    print(info)  # ['first blood', 'lisi', 19, True, [3, 2, 'str1'], None]

    # 序列可相加
    print([1, 2, 4] + [3, 6, 9])  # [1, 2, 4, 3, 6, 9]

    # 乘法
    print([1, 3, 4] * 2)  # [1, 3, 4, 1, 3, 4]
    print('hehe' * 3)  # hehehehehehe

    # len()、min()、max()
    nums = [1, 3, 4, 2, 6, 5]
    print('len: %s, min: %s, max: %s, count(): %s' % (len(nums), min(nums), max(nums), nums.count(5)))  # len: 6, min: 1, max: 6

    # python基础教程补充
    # 1. append()在列表末尾追加元素
    # 2. count()统计某个元素出现次数
    # 3. extend()追加新列表
    # 4. index()第一个匹配元素的索引
    # 5. insert()插入元素到指定索引
    # 6. pop()移除并返回该元素
    # 7. remove()移除列表中第一个匹配的元素
    # 8. reverse(): void逆序列表()
    # 9. reversed(): iterator
    # 10. sort()排序覆盖原列表并返回
    # 11. 高级排序key&reverse
    l = ['jobs', 'catface', 'ash']
    l.sort()
    print(r"['jobs', 'catface', 'ash']的默认排序结果是：", l)  # ['ash', 'catface', 'jobs']
    l.sort(key=len)
    print(l)  # ['ash', 'jobs', 'catface']
    l.sort(key=len, reverse=True)
    print(l)  # ['catface', 'jobs', 'ash']


# -tuple
def test_tuple():
    # tuple是不可变的list，没有append、insert、info[index] = -1等修改操作
    # tuple的每个个元素，指向永远不变，但若某个元素指向一个list，就不能指向其他对象，但这个指向的list本身是可变的
    info = ('zhangsan', 'lisi', 19, 57.46, True, None)
    print(info)  # ('zhangsan', 'lisi', 19, 57.46, True, None)

    # 空tuple
    empty = ()
    print(empty)  # ()

    # 只有一个元素的tuple，需要加个逗号，不然还以为是括号操作呢
    one_1 = (1)
    one_2 = (1,)
    print(one_1, ' || ', one_2)  # 1  ||  (1,)

    # 注意下面是可变tuple，但是实际开发中尽量避免
    values = (1, 2, [3, 4, 5], 6)
    print(values)  # (1, 2, [3, 4, 5], 6)
    values[-2][1] = 99
    print(values)  # (1, 2, [3, 99, 5], 6)
    # tuple的第三个元素是个list，但是list中每个元素的指向是可变的


test_list()
test_tuple()
