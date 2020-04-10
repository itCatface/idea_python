# -枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print('name - %s, member - %s' % (member, member.value))  # value属性是自动赋给成员的int常量，默认从1开始计数

# 精确的控制枚举类型
from enum import Enum, unique


# @unique检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday.Mon.value)
print(Weekday['Mon'])
