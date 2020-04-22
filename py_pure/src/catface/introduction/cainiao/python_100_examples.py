### 1. 四个数字1、2、3、4能组成多少个互不相同且无重复的三位数
import asyncio
from fractions import Fraction
import random
from collections import deque
from datetime import datetime

import time
from functools import reduce
from turtle import Canvas
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import math
import os


def ex1():
    return [x * 100 + y * 10 + z for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if x != y and y != z and x != z]


### 2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def ex2():
    bonus = 0
    profit = int(input('请输入利润：'))
    if profit < 0:
        print('输入的利润无效，请重新输入！')
    elif profit <= 10:
        bonus = profit * 0.1
    elif profit <= 20:
        bonus = 10 * 0.1 + (profit - 10) * 0.075
    elif profit <= 40:
        bonus = 10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05
    elif profit <= 60:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03
    elif profit <= 100:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit - 60) * 0.015
    else:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit - 100) * 0.01
    return bonus


### 3. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def ex3():
    return [n ** 2 - 100 for m in range(1, 168) for n in range(1, m) if m ** 2 - n ** 2 == 168]


### 4. 输入某年某月某日，判断这一天是这一年的第几天？
def ex4():
    year = int(input('enter year:'))
    month = int(input('enter month:'))
    day = int(input('enter day:'))

    month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        r = sum(month_leap[0:month - 1]) + day
    else:
        r = sum(month_not_leap[0:month - 1]) + day
    return 'this is %sth day in %s-%s-%s' % (r, year, month, day)


### 5. 输入三个整数x,y,z，请把这三个数由小到大输出
def ex5():
    s = input('请输入三个数，使用空格分隔')
    return sorted(list(map(int, s.split(' '))))


### 6. 斐波那契数列[F0 = 0(n=0);     F1 = 1(n=1);    Fn = F[n-1]+ F[n-2](n=>2)]
def ex6(n):
    # 方式一
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(a)

    # 方式二
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        r = ex6(n - 1) + ex6(n - 2)
    return r


### 7. 将一个列表的数据复制到另一个列表中
def ex7():
    l1 = [12, '23w', 23, 'ew2', None, 'r2r3']
    l2 = l1.copy()
    l1[0] = 'first change'
    print(l1, '\r\n', l2)


### 8. 输出 9*9 乘法口诀表
def ex8():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%s * %s = %s\t' % (j, i, i * j), end='')
        print()


### 9. 暂停一秒输出
def ex9():
    print('start...')
    time.sleep(1)
    print('end...')


### 10. 暂停一秒输出，并格式化当前时间
def ex10():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


###- 11. 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少
def ex11():
    pass


### 12. 判断101-200之间有多少个素数，并输出所有素数
def ex12():
    return list(filter(lambda x: x not in [i for i in range(101, 200) for j in range(2, i) if not i % j], range(101, 200)))


### 13. 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
def ex13():
    # return [i for i in range(100, 1000) if (i % 10) ** 3 + ((i - i % 10) % 10) ** 3 + ((i - i % 100) / 100) ** 3 == i]
    return [i * 100 + j * 10 + k for i in range(10) for j in range(10) for k in range(10) if i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k]


###- 14. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def ex14():
    pass


### 15. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
def ex15():
    score = int(input('enter your score:'))
    if score >= 90:
        return 'A'
    elif score >= 60:
        return 'B'
    else:
        return 'C'


### 16. 输出指定格式的日期
def ex16():
    return datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S')


### 17. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
def ex17():
    count_english_char = count_blank = count_digital = count_other_char = 0
    s = input('enter something:')
    for i in s:
        if i.isspace():
            count_blank += 1
        elif i.isdigit():
            count_digital += 1
        elif i.isalpha():
            count_english_char += 1
        else:
            count_other_char += 1
    print('英文字母-空格-数字-其它字符的个数分别为:', count_english_char, count_blank, count_digital, count_other_char)


### 18. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
def ex18():
    n = int(input('输入数字：'))
    t = int(input('输入相加次数：'))
    for i in range(1, t):
        n += n * 10
        print(n)


###- 19. 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
def ex19():
    pass


###- 20. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def ex21():
    pass


###- 22. 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
def ex22():
    pass


### 23. 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def ex23():
    for i in range(1, 5):
        print(" " * (4 - i) + "*" * ((i - 1) * 2 + 1))
    for i in range(1, 4):
        print(" " * i + "*" * ((4 - i) * 2 - 1))


### 24. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
def ex24():
    a = 2
    b = 1
    init_f = Fraction(a, b)
    s = init_f
    for i in range(1, 20):
        a, b = a + b, a
        f = Fraction(a, b)
        print('new fraction is:', f, '||a&b:', a, b)
        s += f
    print('分数结果：', s, '|| 小数结果：', s.numerator / s.denominator)


### 25. 求1+2!+3!+...+20!的和
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)


def ex25():
    n = int(input('enter digital:'))
    s = 0
    for i in range(1, n + 1):
        s += jc(i)
    print('%d阶乘之和：', s)


### 26. 利用递归方法求5!
def ex26(n):
    if n == 1:
        return 1
    else:
        return n * ex26(n - 1)


### 27. 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
def ex27(s):
    length = len(s)
    if length < 1:
        return
    else:
        length -= 1
        print(s[length])
        ex27(s[0:length])


### -28. 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
def ex28(n):
    if n == 1:
        return 10
    else:
        return ex28(n - 1) + 2


### 29. 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
def ex29():
    s = input('enter digital:')
    print(len(s), list(reversed(s)))


### 30. 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
def ex30():
    r = True
    s = input('enter digital:')
    for i in range(int(len(s) / 2)):
        if int(s[i]) != int(s[len(s) - i - 1]):
            r = False
    return r


###- 31. 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
def ex31():
    monday = 'Monday'
    tuesday = 'Tuesday'
    wednesday = 'Wednesday'
    thursday = 'Thursday'
    friday = 'Friday'
    saturday = 'Saturday'
    sunday = 'Sunday'
    s = input('enter what day is today:')


### 32. 按相反的顺序输出列表的值
def ex32():
    l = [132, 'awf', False, 'a', None, 23]
    for i in l[::-1]:
        print(i)


### 33. 按逗号分隔列表
def ex33():
    l = [1, 2, 3, 4, 5]
    print(','.join(str(n) for n in l))


### 34. 练习函数调用
def ex34():
    pass
    pass
    pass


### 35. 文本颜色设置
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ex35():
    print(bcolors.WARNING + "警告的颜色字体?" + bcolors.BOLD)


###- 36. 求100之内的素数
def ex36():
    pass


### 37. 对10个数进行排序
def ex37():
    l = [1, 23, 234, 123, 43, 1, 32, 34, 545, 5, 3, 2]
    print(list(sorted(l)))


### 38. 求一个3*3矩阵主对角线元素之和
def ex38():
    r = 0
    m = [[3, 2, 1],
         [4, 3, 2],
         [5, 4, 3]]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j or i + j == 3:
                r += m[i][j]
    print(r)


nums = [324, 19, 153, 324, 25, 13, 54, 3, 34, 3634, 376, 36]


### 39. 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
def ex39():
    l = nums
    print(list(sorted(l)))
    n = int(input('enter digital:'))
    for i, v in enumerate(list(reversed(l))):
        pass


### 40. 将一个数组逆序输出
def ex40():
    for i in range(int(len(nums) / 2)):
        nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
    print(nums)


###- 41. 模仿静态变量的用法
def ex41():
    pass


###- 42. 学习使用auto定义变量的用法
def ex42():
    pass


###- 43. 模仿静态变量(static)另一案例
def ex43():
    pass


### 44. 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
def ex44():
    r = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    l1 = [[1, 2, 3],
          [2, 3, 4],
          [3, 4, 5]]

    l2 = [[3, 2, 1],
          [4, 3, 2],
          [5, 4, 3]]
    for i in range(len(l1)):
        for j in range(len(l2)):
            r[i][j] = l1[i][j] + l2[i][j]
    print(r)


### 45. 统计 1 到 100 之和
def sum(x, y):
    return x + y


def ex45():
    print(reduce(sum, list(range(1, 101))))


### 46. 求输入数字的平方，如果平方运算后小于 50 则退出
def ex46():
    n = int(input('enter digital:'))
    print('result is:', n ** 2)
    if n ** 2 < 50:
        exit()
    else:
        ex46()


### 47. 两个变量值互换
def ex47(a='r', b=32):
    print('a, b:', a, b)
    a, b = b, a
    print('a, b:', a, b)


### 48. 数字比较
def ex48():
    n1 = int(input('enter number 1:'))
    n2 = int(input('enter number 2:'))
    if n1 > n2:
        print('%s 大于 %s' % (n1, n2))
    elif n1 == n2:
        print('%s 等于 %s' % (n1, n2))
    else:
        print('%s 小于 %s' % (n1, n2))
    pass


### 49. 使用lambda来创建匿名函数
def ex49():
    return reduce(lambda x, y: x + y, list(range(1, 101)))


### 50. 输出一个随机数
def ex50():
    r = random.uniform(10, 20)  # 10-20随机数
    print(r)
    r = random.random()  # 0-1随机数
    print(r)
    r = random.randint(10, 20)  # 10-20随机整数
    print(r)
    r = random.choice([x for x in range(100, 200) if x % 2 == 0 and x % 3 != 0 and x % 4 != 0])  # choices输出一个随机数的list
    print(r)


### 51. 学习使用按位与 &   52. 学习使用按位或 |   53. 学习使用按位异或 ^  54. 取一个整数a从右端开始的4〜7位    55. **学习使用按位取反~**
def ex51():
    print('9 & 4:', 9 & 4)
    print('7 << 2:', 7 << 2)

    print('9 | 3:', 9 | 3)

    print('9 ^ 3:', 9 ^ 3)

    print('取一个整数9从右端开始的4〜7位:', (9 >> 3) & ~(~0 << 4))

    print('~9:', ~9)


### 56. 画图，学用circle画圆形
def ex56():
    x = y = np.arange(-11, 11, 0.1)
    x, y = np.meshgrid(x, y)
    # 圆心为（0，0），半径为1-10
    for i in range(1, 11):
        plt.contour(x, y, x ** 2 + y ** 2, [i ** 2])
        # 如果删除下句，得出的图形为椭圆
        plt.axis('scaled')
    plt.show()


### 57. 画图，学用line画直线
def ex57():
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = y0 = 263
    x1 = y1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    x0 = y0 = 263
    y1 = 275
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5
    mainloop()


### 58. 画图，学用rectangle画方形
def ex58():
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0 = y0 = 263
    x1 = y1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    canvas.pack()
    mainloop()


### 59. 画图，综合例子
def ex59():
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()


### 60. 计算字符串长度
def ex60():
    s = input('enter something:')
    print('the str\'s length is:', len(s))


###-- 61. 打印出杨辉三角形（要求打印出10行如下图）
def ex61():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


### 62. 查找字符串
def ex62():
    s1 = 'afwqe撒旦法吴青峰23 afasdf容器r23日3人3rfqqfa'
    s2 = '23'
    return s1.find(s2)


### 63. 画椭圆
def ex63():
    x, y = 360, 160
    top = bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()


### 64. 利用ellipse 和 rectangle 画图
def ex64():
    canvas = Canvas(width=400, height=600, bg='white')
    left, right, top, num = 20, 50, 50, 15
    for i in range(num):
        canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
        canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
        canvas.create_rectangle(20 - 2 * i, 20 - 2 * i, 10 * (i + 2), 10 * (i + 2))
        right += 5
        left += 5
        top += 10
    canvas.pack()
    mainloop()


### 65. 一个最优美的图案

class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0


points = []


def ex65():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius,
                       xcenter + radius, ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)

    canvas.pack()
    mainloop()


### 66. 输入3个数a,b,c，按大小顺序输出
def ex66():
    n1 = int(input('num1:'))
    n2 = int(input('num2:'))
    n3 = int(input('num3:'))
    for i in list(sorted([n1, n2, n3])):
        print(i)


### 67. 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
def ex67():
    l = list(map(int, input('enter some nums:').split(' ')))
    for i, v in enumerate(l):
        if v == max(l):
            l[0], l[i] = v, l[0]
        if v == min(l):
            l[i], l[len(l) - 1] = l[len(l) - 1], v
    return l


### 68. 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
def ex68(m=3):
    l = [3, 5, 2, 6, 7, 2, 1, 9, 4]
    l2 = l3 = l4 = l.copy()

    print('l2:', l2[-m:] + l2[:-m])

    for _ in range(m):
        l3.insert(0, l.pop(-1))
    print('l3:', l3)

    print(deque(l2))
    # print('l4:', list(deque(l).rotate(m)))
    pass


### 69. 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
def ex69():
    pass


### 70. 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
def ex70():
    pass
    pass
    pass


### 71. 编写input()和output()函数输入，输出5个学生的数据记录
def ex71(n=5):
    students = []
    for _ in range(n):
        pass


### 72. 创建一个链表
def ex72():
    l = []
    for i in range(5):
        l.append(int(input('enter num%s:' % (i + 1))))
    return l


### 73. 反向输出一个链表
def ex73():
    return list(reversed(nums))


### 74. 列表排序及连接
def ex74():
    l1 = [1, 3, 2, 7, 5]
    l2 = [6, 4, 9, 7, 0]

    print('sort:', list(sorted(l1)))
    print('+:', l1 + l2)


### 75. 放松一下，算一道简单的题目
def ex75():
    return reduce(lambda x, y: x + y, [i for i in range(4) if i % 2 != 0])


### 76. 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def ex76(n=5):
    if n % 2 == 0:
        return reduce(lambda x, y: x + y, list(map(lambda x: 1 / x, [x for x in range(1, n + 1) if x % 2 == 0])))
    else:
        return reduce(lambda x, y: x + y, list(map(lambda x: 1 / x, [x for x in range(1, n + 1) if x % 2 != 0])))


### 77. 循环输出列表
def ex77():
    for i, v in enumerate(nums):
        print('the %s of nums\'s value is:', v)


### 78. 找到年龄最大的人，并输出。请找出程序中有什么问题
def ex78():
    persons = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    print(persons.values())


### 79. 字符串排序
def ex79():
    pass


### 80. 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，
# 拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、
# 第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
def ex80():
    pass


### 81. 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
# 求??代表的两位数，及809*??后的结果
def ex81():
    pass


### 82. 八进制转换为十进制
def ex82():
    pass


###- 83. 求0—7所能组成的奇数个数
def ex83():
    l = [n1 * 1000000 + n2 * 100000 + n3 * 10000 + n4 * 1000 + n5 * 100 + n6 * 10 + n7 for n1 in range(10) for n2 in range(10) for n3 in range(10) for n4 in range(10) for n5 in range(10) for n6 in range(10) for n7 in range(10) if
         (n1 * 1000000 + n2 * 100000 + n3 * 10000 + n4 * 1000 + n5 * 100 + n6 * 10 + n7) % 2 != 0]
    return len(l)


### 84. 连接字符串
def ex84():
    names = ['ashy', 'yi', 'uzi', 'mlxg', 'smlz']
    print('join:', ','.join(names))

    s1 = '123'
    s2 = 'qwer'
    print('+:', s1 + s2)


###- 85. 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
def ex85():
    n = int(input('enter an odd:'))
    if n % 2 == 0:
        print('enter an odd plz!')
    else:
        for i in range(1, 50):
            print(int('9' * i) % n)
            if int('9' * i) >= n and int('9' * i) % n == 0:
                return i
        return 'no result!'


### 86. 两个字符串连接程序[+]
def ex86():
    pass
    pass
    pass


### 87.
def ex87():
    pass


### 88. 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
def ex88():
    for _ in range(7):
        j = random.randint(1, 51)
        print('num is:%s\t%s' % (j, '*' * j))


### 89. 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
def ex89():
    pass


### 90. 列表使用实例
def ex90():
    pass
    pass
    pass


### 91. 时间函数举例1
def ex91():
    pass
    pass
    pass


### 92. 时间函数举例2
def ex92():
    pass
    pass
    pass


### 93. 时间函数举例3
def ex93():
    pass
    pass
    pass


### 94. 时间函数举例4,一个猜数游戏，判断一个人反应快慢
def ex94():
    pass


### 95. 字符串日期转换为易读的日期格式
def ex95():
    pass


### 96. 计算字符串中子串出现的次数
def ex96():
    pass


### 97. 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
def ex97():
    file_path = '../../introduction_dir/cainiao_100.txt'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path, 'a', encoding='utf-8') as f:
        pass


### 98. 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
def ex98():
    with open('../../introduction_dir/test.txt', 'a', encoding='utf-8') as f:
        f.write(input('enter something:').upper())


### 99. 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
def ex99():
    s1 = s2 = ''
    with open('../../introduction_dir/testB.txt', 'r', encoding='utf-8') as f:
        s1 = f.read()
    with open('../../introduction_dir/test.txt', 'r', encoding='utf-8') as f:
        s2 = f.read()
    return reduce(lambda x, y: x + y, sorted(s1 + s2))


### 100. 列表转换为字典
def ex100():
    l1 = ['ahri', 'akali', 'alistar', 'amumu', 'anivia']
    l2 = [1, 3, 5, 7, 9]
    return dict(zip(l1, l2))


if __name__ == '__main__':
    # print(int('9' * 3) // 33)
    ex28(10)
