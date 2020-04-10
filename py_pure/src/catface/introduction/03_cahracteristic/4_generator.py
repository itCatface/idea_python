# *-生成器[边循环边计算]
# 生成器的创建方案一：将一个列表生成式的[]改成()
g = (x * x for x in range(10))
print(type(g))  # <class 'generator'>
for i in range(7):
    print(next(g))

print('---')

for x in g:
    print(x)

print('---')


# 若函数定义中包含关键字yield[屈服、生产、放弃、收益、中断],则这个函数是一个generator*******************************
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


print('------>fib(6)')
fib(6)


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # print(b)
        a, b = b, a + b
        n += 1
    return 'done'


# 拿不到generator的return返回值
for x in fibonacci(10):
    print(x)

print('---')

f = fibonacci(8)
while 1 > 0:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print('generator return value is: ', e.value)
        break
