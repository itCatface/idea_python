# -*协程[python对协程的支持是通过generator实现的 | 子程序就是协程的一中特例]


# consumer函数是一个生成器(协程|子程序)
def consumer():
    r = ''
    while True:
        n = yield r  # 3. consumer通过yield拿到消息后处理并通过yield将结果返回
        if not n:
            return
        print('[CONSUMER] consuming %s...' % n)
        r = '200 OK'


def producer(c):
    c.send(None)  # 1. 启动生成器
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 2. 生产东西后切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # producer不生产后关闭consumer结束整个过程


c = consumer()
producer(c)
