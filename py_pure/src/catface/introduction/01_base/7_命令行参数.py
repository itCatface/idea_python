import fileinput
import getopt
import getpass
import sys
import argparse

# -处理命令行参数
# 使用argv[只能从外部运行程序并给出参数-C:\Users\xxx>python C:\xxx\Desktop\7_命令行参数.py 11 22 33 44]
import click
import fire


def use_argv():
    args = sys.argv
    print("args's type:", type(args), '||args:', args)
    for k, arg in enumerate(args):
        print('第%s个参数值为%s' % (k, arg))


# 使用stdin[读取标准输入]
def use_stdin():
    for k, line in enumerate(sys.stdin):
        print('第%s行值为%s' % (k, line))


# 使用fileinput[读取标准输入]
def use_fileinput():
    for line in fileinput.input():
        print('line值为', line)


# 使用getpass[读取密码]
def use_getpass():
    usr = getpass.getuser()
    pwd = getpass.getpass('your password: ')
    print('usr: %s, pwd: %s' % (usr, pwd))


# 使用argparse[解析命令行参数]
def use_argparse():
    parser = argparse.ArgumentParser(description='this is description')
    parser.add_argument('-v', action='store', default='v0.1', dest='version', help='app-version')
    parser.add_argument('-d', action='store', default='description', help='description')
    parser.add_argument('-s', action='store_true', default=False, help='save?')  # store_xx[将参数转换为xx]

    args = parser.parse_args()
    print('-v:', args.version)  # dest[用于解析的参数别名]
    print('-d:', args.d)
    print('-s:', args.s)  # 只要传-s就是True不用加额外参数


# 使用click[解析命令行参数-比argparse快速和简单]
@click.command()
@click.option('-v', default='v0.1', help='app-version')
@click.option('-d', default='description', help='description')
@click.option('-s', default=False, type=bool, help='save?')
def use_click(v, d, s):
    print('v:', v)
    print('d:', d)
    print('s:', s)


# 使用fire[python xx.py 9 5]
def use_fire():
    fire.Fire(lambda x, y: x + y)


# 使用getopt[配合sys.argv]

if __name__ == '__main__':  # use_argv()
    # use_stdin()
    # use_fileinput()
    # use_getpass()
    # use_argparse()
    # use_click()
    use_fire()
