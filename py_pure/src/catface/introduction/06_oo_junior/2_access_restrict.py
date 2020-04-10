# -访问限制
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # 检查分数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            return ValueError('invalid score!')

    def get_score(self):
        return self.__score

    def print(self):
        print('name: %s, score: %s' % (self.__name, self.__score))


s = Student('kobe', 8)
print('s.get_name:', s.get_name())
print('s.get_score:', s.get_score())
s.set_score(24)
print('s.get_score:', s.get_score())
print(s.set_score(-1))
# 这里只是给实例s新增了__score变量
s.__score = 99
print('s.get_score:', s.get_score(), ' || s.__score:', s.__score)
