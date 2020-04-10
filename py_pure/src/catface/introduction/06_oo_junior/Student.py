class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s, %s' % (self.name, self.score))


s1 = Student('zhangsan', 27)
s2 = Student('lisi', 31)
s2.age = 7
print(s2.age)
s1.print_score()


# 1. issubclass(subclz, superclaz)检查是否是子类

# 2. subclz.__bases__得到其基类们

# 3. isinstance()判断是否是某类的实例


class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('''i'm eating...''')
            self.hungry = False
        else:
            print('''i'm not hungry...''')


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'aaaooo'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
