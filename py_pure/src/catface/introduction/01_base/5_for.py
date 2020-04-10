# -循环
def test_for():
    # for
    nums = (1, 2, 3, 4, 5)
    sum = 0
    for x in nums:
        sum += x
    print(sum)  # 15
    for i, v in enumerate(nums):
        print('第%d个位置的值为%d' % (i, v))  # 第0个位置的值为1\n第1个位置的值为2...

    # range
    nums = list(range(10))  # range(x): 生成一个整数序列 | list(range(x)): 通过list()将整数序列转换为list
    print('range(5):', range(5), 'nums: ', nums)  # range(0, 5) nums:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # while
    sum = 0
    num = 100
    while num > 0:
        sum += num
        num -= 1
    print(sum)  # 5050

    # 练习：循环打印['zhangsan', ...]
    names = ['zhangsan', 'lisi', 'wanger', 'mazi']
    for name in names:
        print('hi:', name)

    # break[提前退出循环] & continue[结束本轮循环，直接开始下一轮循环]
    n = 0
    while n < 5:
        n += 1
        if n > 3:
            # break可退出循环
            break
        print(n)  # 1 2 3

    n = 0
    while n < 6:
        n += 1
        if n % 2 == 0:
            # continue结束本次循环并开始下一轮循环，通常配合if使用
            continue
        print(n)  # 1 3 5


test_for()
