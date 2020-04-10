# -匿名函数
# --ex1
l = [1, 3, 5, 7, 9]
r = map(lambda x: x * x, l)
print(list(r))

# --ex2
print('匿名函数结果：', list(map((lambda x: x * 2), l)))

# --ex3. 可以把匿名函数作为返回值返回
f = lambda x, y: x * y
print('使用匿名函数计算：', f(2, 3))


# lambda x: x * x --> def f(x): return x * x


# --ex4. 改造以下代码
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

r = filter(lambda x: x % 2 == 1, range(1, 20))
print(list(r))
