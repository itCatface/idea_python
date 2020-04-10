# -装饰器decorator[返回一个函数的高阶函数]


# 在函数执行前添加log
def log(func):
    def wrapper(*args, **kw):  # 可接受任意参数调用
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)

    return wrapper


from datetime import datetime


@log
def get_dt():
    dt = datetime.now()
    print(dt)


get_dt()


# 自定义log内容
def log(txt):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (txt, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('自定义log=>')
def get_dt2():
    dt = datetime.now()
    print(dt)


get_dt2()
print(get_dt2.__name__)  # wrapper


# 解决方法名问题


def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log1
def dt():
    print(datetime.now())


dt()


def log2(txt):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (txt, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('test time')
def dt2():
    print(datetime.now())


dt2()
print(dt2.__name__)  # dt2

#############################################################################################################################33
print('----------------------\r\n')


# --1. 普通的装饰器[打印调用的方法名]
def log(func):
    def wrapper(*args, **kw):
        print('call %s()↓↓↓' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def f():
    print('测试一下装饰器函数')


f()  # log(f)


# --2. 带参数的装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('call %s() && desc is %s' % (func.__name__, text))
            return func(*args, **kw)

        return wrapper  # 需将原始函数的__name__等属性复制到wrapper()函数中

    return decorator


@log('我是说明')
def f():
    print('测试一下带参数的装饰器')


f()  # log('text')(f)
print('f.__name__ is:', f.__name__)  # wrapper[如代码中注释：需将原始函数的__name__等属性复制到wrapper()函数中]，解决方案如下

# --3. 装饰器装饰后方法名属性等问题
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()↓↓↓' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def f():
    print('测试一下装饰器函数')


print('f.__name__ is:', f.__name__)  # f


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s() && desc is %s' % (func.__name__, text))
            return func(*args, **kw)

        return wrapper  # 需将原始函数的__name__等属性复制到wrapper()函数中

    return decorator


@log('我是说明2')
def f():
    print('测试一下带参数的装饰器')


print('f.__name__ is:', f.__name__)  # f

# --ex1. 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        f = func(*args, **kw)
        print('%s() 执行时间为：%s' % (func.__name__, time.time() - t))
        return f

    return wrapper


@log
def f():
    time.sleep(1)
    print('测试打印执行时间的装饰器')


f()
