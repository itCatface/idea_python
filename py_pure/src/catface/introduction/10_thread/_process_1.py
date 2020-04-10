# A. 多进程

# import os
#
# print(os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#
# pid = os.fork()
# if 0 == pid:
#     print('child process: %s, parent process: %s' % (os.getpid(), os.getppid()))
# else:
#     print('%s, just child process: %s' % (os.getpid(), pid))


### B. 以上的fork只能在非windows系统下使用

from multiprocessing import Process
import os


def run_proc(name):
    print('run child process %s (%s)' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('parent process is: %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start.')
#     p.start()
#     # join()方法等子线程结束后再继续运行，常用于进程间同步
#     p.join()
#     print('child process end.')

### C. Pool
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %0.2f seconds.' % (name, (end - start)))


# if __name__ == '__main__':
#     print('\r\n')
#     print('parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('all subprocess done.')


### D. 子进程
import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('exit code:', r)

### E. 进程间通信
from multiprocessing import Process, Queue
import os, time, random


# 写数据
def write(q):
    print('process to write: %s' % os.getpid())
    for v in ['a', 'b', 'c']:
        print('put %s to sequence...' % v)
        q.put(v)
        time.sleep(random.random())


# 读数据
def read(q):
    print('process to read %s' % os.getpid())
    while True:
        v = q.get(True)
        print('get %s from sequence.' % v)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
