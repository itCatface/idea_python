# -继承
class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running...')


class Cat(Animal):
    def run(self):
        print('cat is running...')


# -多态
def run_open(animal):
    animal.run()


class Timer(object):
    def run(self):
        print('start running...')


a = Animal()
d = Dog()
c = Cat()
run_open(a)
run_open(d)
run_open(c)

# python符合动态语言的鸭子类型==>不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
d = Timer()
run_open(d)
