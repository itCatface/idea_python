import math

# -内置函数[abs() dict() help() min() setattr() all() dir() hex() next() slice() any() divmod() id() object() sorted() ascii() enumerate() input() oct() staticmethod() bin() eval() int() open() str() bool() exec() isinstance() ord() sum() bytearray() filter() issubclass() pow() super() bytes() float() iter() print() tuple() callable() format() len() property() type() chr() frozenset() list() range() vars() classmethod() getattr() locals() repr() zip() compile() globals() map() reversed() __import__() complex() hasattr() max() round() delattr() hash() memoryview() set() ]


# -调用常用python内置函数
# help()
print('help(input):', help(input))
# abs() | max() | min() | hex()
print(abs(-100))  # 100

t = (-1, 1, 3, 2)
print('max, min is: %s, %s', (max(t), min(t)))  # (3, -1)

print(hex(255), hex(-65535))  # 0xff -0xffff

# range()
for x in range(10, 30, 5):
    print(x)

# 数据类型转换
print(int('1234'))
print(float('12.34'))
print(str(100))
print(bool(0))

# 变量abs_copy指向abs函数，所以也可以通过abs_copy调用abs函数[即个给abs函数起了一个别名]
abs_copy = abs
print('-3的绝对值：', abs_copy(-3))  # -3的绝对值： 3


# -python的返回多值其实是一个tuple[语法上返回一个tuple可省略括号]
def _24_def(x, y):
    return x - y, x + y, x * y, x / y


print('_24_def(3, 5)的结果：', _24_def(3, 5))  # _24_def(3, 5)的结果： (-2, 8, 15, 0.6)


# 练习：求一元二次方程的两个根
def p_25(a, b, c):
    z = b ^ 2 - 4 * a * c
    if z == 0:
        return (-b) / (2 * a)
    elif z > 0:
        r1 = (-b + math.sqrt(z)) / (2 * a)
        r2 = (-b - math.sqrt(z)) / (2 * a)
        return r1, r2
    else:
        return


print('p_25(1, -3, 4)的结果：', p_25(1, -3, 4))  # p_25(1, -3, 4)的结果： (3.4364916731037085, -0.4364916731037085)


# -函数的参数[正常定义的必选参数、默认参数、可变参数、关键字参数]
# 必选参数在前，默认参数在后
# 默认参数必须指向不变对象
def _26_def(x, n=2):
    result = 1
    while n > 0:
        result *= x
        n -= 1
    return result


def _27_def(name, age, city='合肥', sex='girl'):
    print('name:', name, 'age:', age, 'city:', city, 'sex:', sex)


# _27_def('zhangsan', 27, '纽约')  # name: zhangsan age: 27 city: 纽约 sex: girl
# _27_def('zhangsan', 27, sex='boy')  # name: zhangsan age: 27 city: 合肥 sex: boy


# 默认参数必须指向不变对象！
def add_end(l=[]):
    l.append('END')
    return l


# 优化上面的函数
def add_end_optimize(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


# -可变参数
# 可变参数会将list或tuple的元素变成可变参数->func(*(1, 2, 3))
# 会自动组装成一个tuple
# python允许在list或tuple前加一个*，把list或tuple的元素编程可变参数传进去
def _28_def(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


# print(_28_def(1, 2, 3))       # 6
# print(_28_def(*[2, 3, 4]))    # 9
# print(_28_def(*(3, 4, 5)))    # 12


# -关键字参数[可扩展函数功能]
# 会自动组装成dict->func(**{'1':1, '2':2, '3':3})
# 注意：kv获得的dict是extra的拷贝，对kv做改动不会影响到函数外的extra
def _29_def(name, age, **kv):
    print('name:', name, 'age:', age, 'kv:', kv)


# _29_def('zhangsan', 18)                           # name: zhangsan age: 18 kv: {}
# _29_def('lisi', 19, city='hefei', xex='male')     # name: lisi age: 19 kv: {'city': 'hefei', 'xex': 'male'}
# extra = {'city': 'demaxiya', 'job': 'adc'}
# _29_def('wanger', 20, **extra)                     # name: wanger age: 20 kv: {'city': 'demaxiya', 'job': 'adc'}


# 限制关键字参数[可以有缺省值]
# *, 后面的参数是必须要传的
def _30_def(name, age, *, city='hefei', sex):
    print('name:', name, 'age:', age, 'city:', city, 'sex;', sex)


# _30_def('zhangsan', 24)                               # TypeError: _30_def() missing 1 required keyword-only argument: 'sex'
# _30_def('zhangsan', 24, sex='girl')                   # name: zhangsan age: 24 city: hefei sex; girl
# _30_def('zhangsan', 24, city='china', sex='girl')     # name: zhangsan age: 24 city: china sex; girl


# 命名关键字参数必须传入参数名
# 可变参数后跟着的命名关键字参数不再需要特殊分隔符*
def _31_def(name, age, *city, sex):
    print('name:', name, 'age:', age, 'city:', city, 'sex:', sex)

# _31_def('zhangsan', 29, 2, 2, sex='girl')  # name: zhangsan age: 29 city: (2, 2) sex: girl

# -参数组合[必选参数、默认参数、可变参数tuple、命名关键字参数(限制关键字参数的名字: *, )和关键字参数**dict]
# def f1(a, b, c=0, *args, **kw) | def f2(a, b, c=0, *, d, **kw)

# f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
# f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
# f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
