# -使用模块

import sys


def f():
    print('sys.path is:', sys.path)
    var = sys.argv
    if len(var) == 1:
        print('len(var) == 1')
    elif len(var) == 2:
        print('len(var) == 2')
    else:
        print('len(var) >2')


if __name__ == '__main__':
    f()

# -安装模块==>pip install xxx
