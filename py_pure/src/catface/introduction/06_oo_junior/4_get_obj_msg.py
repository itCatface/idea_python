# -获取对象信息
# 1. type()[判断对象类型][能用type判断的基本类型也能用isinstance判断]
# 2. isinstance()[判断class类型]
print('type(22):', type(22))  # type(22): <class 'int'>


class Animal(object):
    pass


class Dog(Animal):
    pass


print('isinstance(Dog(), Animal):', isinstance(Dog(), Animal))

print('isinstance(22, str):', isinstance(22, str))

# 3. 判断一个变量是否是某些类型中的一种
print('isinstance([1, 2, 3], (list, tuple))', isinstance([1, 2, 3], (list, tuple)))

# -dir()[获取一个对象的所有属性和方法]
print('dir(\'aaa\')', dir('aaa'))

# -getattr()、setattr()、hasattr()
d = Dog()
# print(getattr(d, 'name')) # AttributeError
print(getattr(d, 'sex', 'no attr: sex'))
print(hasattr(d, 'score'))
setattr(d, 'age', 17)
print(hasattr(d, 'age'))
print(getattr(d, 'age'))


# 读取图片流
def read_data(f):
    pass


def read_img(f):
    if hasattr(f, 'read'):
        return read_data(f)
    return None
