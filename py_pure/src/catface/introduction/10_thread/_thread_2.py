# 求素数
import math

from dask.dataframe.io.io import lock

for i in range(2, 20):
    for j in range(2, i):
        if i / j == 0:
            break
        else:
            print(i)

print(2 / 4)

# for i in range(2, 20):
#     for j in range(3, i):
#         if i == j:
#             break
#         if j / i == 0:
#             break
#         else:
#             print(i)

# for x in range(2, math.ceil(math.sqrt(x))):
#     for i in range(2, x):
#         if x / i == 0:
#             break
#         else:
#             print(x)
#
# print(2 / math.sqrt(2))


####################################################################################################### 多线程
## 1. 多线程
import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

## 2. Lock
# 1. 不加锁
balance = 0


def change(n):
    global balance
    balance += n
    balance -= n


# def run(n):
#     for i in range(100_000):
#         change(n)

# 2. 加锁
def run(n):
    for i in range(100_000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run, args=(513,))
t2 = threading.Thread(target=run, args=(876,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
