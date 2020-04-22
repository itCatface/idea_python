# -输入和输出
from fractions import Fraction

width = int(input('请输入宽：'))
height = int(input('请输入高：'))
# ,在打印时会用空格代替
print('矩形面积：', '%s * %s = %s' % (width, height, width * height))

# -数据类型
a = 1
b = 1.11
b1 = 0xf
b2 = 1.2e-5
c = 'I\'m \"OK\"!'
# r'xxx': 内部的字符串(xxx)默认不转义
c1 = r'I\'m \"OK\"!'
d = '''00
11
22
'''
e1 = 3 > 5
e2 = 4 > 1
e3 = e1 and e2
e4 = e1 or e2
e5 = not e1
# 空值,不能理解为0
f = None

print(a, b, b1, b2, c, c1, d, e1, e2, e3, e4, e5, f)

# -变量和常量[一般全大写,可修改,纯靠自觉]
a = 'abc'
b = a
a = 'xyz'
print('a, b: ', a, b)

PI = 3.1415926
print(PI)

# -简单运算
print(10 / 3)
print(10 // 3)
print(10 % 3)

# -Python对整数和浮点数无大小限制[但超过一定范围就直接表示为无限大(inf)]

# -分数
f = Fraction(2, 3)
print(f, f.denominator, f.numerator, type(f))
# 小数转分数
f1 = float.as_integer_ratio(0.75)
f2 = float.as_integer_ratio(0.33)
print(f1, f2)
