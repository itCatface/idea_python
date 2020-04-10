# -filter[惰性计算]: 接收一个函数和一个序列，并将函数一次作用于每个元素，然后返回值True/False决定是否保留该元素


# --1. 过滤掉所有奇数
def is_odd(x):
    return x % 2 == 0


r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(list(r))  # [2, 4, 6]


# --2. 过滤掉所有空串
def not_empty(x):
    return x and x.strip()


r = filter(not_empty, ['A', '', 'B', None, ' C ', '  '])
print(list(r))  # ['A', 'B', ' C ']


# --*3. 求素数[埃氏筛法]
def odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def prime_num():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


for n in prime_num():
    if n < 30:
        print(n)  # 2 \n 3 \n 5...
    else:
        break


# 4. 求回数
def xyx_num(num):
    s = str(num)
    for x in range((len(s) + 1) // 2):
        if s[x] != s[(len(s) - x - 1)]:
            return False
        return True


r = filter(xyx_num, range(1, 100))
print(list(r))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
