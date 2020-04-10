# -@property[既能检查参数，又可以用类似属性这样简单的方式来访问类的变量]


# 常规getter&setter
class Student(object):

    def __init__(self):
        pass

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100')
        self._score = score

    def get_score(self):
        return self._score


s1 = Student()
# s1.set_score('78')
# s1.set_score(789)
s1.set_score(78)
print("s1's get_score:", s1.get_score())


# 使用@property将方法变成属性调用
class Animal(object):

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be an integer')
        if age < 0:
            raise ValueError('age must > 0')
        self._age = age


a1 = Animal()
# a1.age = '12'
# a1.age = -1
a1.age = 1
print("a1's age:", a1.age)


# ex1. 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    # 只读属性==>只定义getter方法，不定义setter方法
    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 768
s.height = 1024
print("s's resolution is:", s.resolution)
