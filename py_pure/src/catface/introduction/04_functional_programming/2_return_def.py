l = [1, 2, 3]


# --1.简单求和函数
def sum(*args):
    r = 0
    for v in args:
        r += v
    return r


print('sum函数：', sum, 'list求和结果为：', sum(*l))


# *--2.返回函数
def sum_lazy(*args):
    def sum():
        r = 0
        for v in args:
            r += v
        return r

    return sum  # 闭包 --> 相关参数和变量都保存在返回的函数中


f1 = sum_lazy
f2 = sum_lazy(*l)  # 每次调用都会返回一个新的函数(且分别的调用结果互不影响)
f3 = f2()
# 调用lazy_sum()时返回的是求和函数
# 调用lazy_sum()()函数时才真正计算求和的结果
print('sum_lazy：', sum_lazy, 'sum_lazy()：', sum_lazy(), 'sum_lazy(*l)：', sum_lazy(*l), 'list求和结果[sum_lazy(*l)()]为：', sum_lazy(*l)())
f2_2 = sum_lazy(*l)
print('f2 == f2_2:', f2 == f2_2)


# *-闭包
# --*3.案例
def count():
    ls = []
    for v in range(1, 4):
        def f():
            return v * v

        ls.append(f)
    return ls


f1, f2, f3 = count()
print('f1:', f1, 'f2:', f2, 'f3:', f3)
print(f1(), f2(), f3())


# 返回的函数引用了变量v，其不会立刻执行，等3个函数都返回时，他们所引用的变量v已经变成3，因此最终结果为9
# // [闭包]返回函数不要引用任何循环变量，或者后续会发生变化的量
# --4. 如果一定要引用循环变量，可参考如下操作
def count():
    def f(j):
        def g():
            return j * j

        return g

    ls = []
    for v in range(1, 4):
        ls.append(f(v))
    return ls


f1, f2, f3 = count()
print('f1:', f1, 'f2:', f2, 'f3:', f3)
print(f1(), f2(), f3())


# --5. 使用lambda简写上述代码


# --6. 利用闭包返回一个计数器函数，每次调用它返回递增整数
def create_counter():
    def counter(l=[]):
        l.append(0)
        return len(l)

    return counter


counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
