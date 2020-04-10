# -条件判断
def test_if():
    # 赋值方式 --> 序列解包
    x, y = 1, 3
    print('x: %d, y: %d' % (x, y))  # x: 1, y: 3
    # 交换x，y
    x, y = y, x
    print('x: %d, y: %d' % (x, y))  # x: 3, y: 1

    # 赋值方式 --> 链式赋值
    c = d = e = 1
    print('c: %d, d: %d, e: %d' % (c, d, e))  # c: 1, d: 1, e: 1

    # 布尔False可用如下表示 --> False, None, 0, "", (), [], {}

    # if语句可用if ... elif ... elif ... else表达

    # 注意嵌套if

    # 比较运算符 --> ==, >=, <=, >, <, !=, is | is not(是不是同一个对象) in | not in(是成员)

    age = int(input('请输入年龄：'))
    if age < 27:
        print('你比我小')
    elif age < 50:
        print('阿姨你好')
    else:
        print('大伯您好')

    # 联系：计算BMI(体重除以身高的平方)
    weight = input('enter your weight(单位kg):')
    height = input('enter your height(单位m):')

    # weight、height是字符串,需要转换成可运算数据类型
    bmi = float(weight) / float(height) / float(height)
    print("经计算，你的BMI：", bmi)
    if bmi < 18.5:
        print('过轻')
    elif bmi < 25:
        print('正常')
    else:
        print('过胖')


test_if()
