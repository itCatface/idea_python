# -类和实例
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print('name: %s, score: %s' % (self.name, self.score))


s = Student('iverson', 3)
s.print()

# [VS静态语言]python允许实例变量绑定任何数据
s.age = 8
print("iverson's age:", s.age)
# s1 = Student('ashe', 17)
# print("sahe's age:", s1.age)
