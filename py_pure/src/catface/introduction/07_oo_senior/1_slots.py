# coding = utf-8
# /usr/bin/env/ python


class Animal(object):
    pass


a = Animal()
# 1. 给实例绑定属性
a.name = 'ashe'
print("a's name", a.name)


# 2. 给实例绑定方法[对其他实例无作用]
def set_age(self, age):
    self.age = age


from types import MethodType

a.set_age = MethodType(set_age, a)

a.set_age(17)
print("a's age", a.age)


# a1 = Animal()
# a1.set_age(19)
# print("a1's age", a1.age)


# 3. 给class绑定方法
def set_name(self, name):
    self.name = name


Animal.set_name = set_name

a1 = Animal()
a1.set_name('ashy')
print("a1's name", a1.name)


# -使用__slots__[限制实例的属性]
class Student(object):
    # 只允许对Student实例添加name和score属性
    __slots__ = ('name', 'score')


s1 = Student()
s1.name = 'james'
s1.score = 100


# s1.sex = 'male'  # AttributeError


def set_sex(self, sex):
    self.sex = sex


Student.set_sex = set_sex

# s1.set_sex('girl')# AttributeError
# print("s1's sex:", s1.sex)  # AttributeError


# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
