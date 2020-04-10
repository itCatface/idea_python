# 多重继承[python允许，java是单一继承的语言不允许多重继承]
class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('running...')


class FlyableMixIn(object):
    def fly(self):
        print('flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Parrot(Bird, FlyableMixIn):
    pass


class Person(Mammal, RunnableMixIn, FlyableMixIn):
    pass
