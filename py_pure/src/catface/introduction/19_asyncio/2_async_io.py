# /usr/bin/env python

import asyncio


# ex1. 协同需要等待
@asyncio.coroutine
def hello():
    print('hello catface')
    # 异步调用asyncio.sleep()
    r = yield from asyncio.sleep(3)
    print('hello again!')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

### 用Task封装两个coroutine
import threading, asyncio


# ex2. 两个coroutine是由同一个线程并发执行
@asyncio.coroutine
def hello():
    print('hello catface! - %s' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('hello again! - %s' % threading.currentThread())


# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# ex3. 测试异步网络IO操作
@asyncio.coroutine
def get(host):
    print('get %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
tasks = [get(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
