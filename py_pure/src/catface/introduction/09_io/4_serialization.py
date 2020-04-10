# -序列化
import pickle

d = dict(name='Bob', age=20, score=88)

# 1. pickle.dumps()方法将任意对象序列化成一个bytes
pickle.dumps(d)

with open('../../introduction_dir/se.txt', 'wb') as f:
    # 2. pickle.dump()将对象序列化后写入一个文件中
    pickle.dump(d, f)  # 序列化

with open('../../introduction_dir/se.txt', 'rb') as f:
    # 3. pickle.load()方法从一个file-like Object中直接反序列化出对象
    print(pickle.load(f))  # 反序列化

# -json
## 1. json和python内置的数据类型对应
# {}            dict
# []            list
# "string"      str
# 1234.56       int或float
# true/false    True/False
# null          None
import json

j = json.dumps(d)
print(j)  # 序列化为json，返回一个str，内容就是标准的json

s = json.loads(j)
print(s)  # 反序列化json


# -json进阶：序列化对象
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 增加转换函数
def user2dict(s):
    return {'name': s.name, 'age': s.age}


# user实例先被转换成dict，再被序列化为json
u = User('zhangsan', 17)
j = json.dumps(u, default=user2dict)
print(j)

# 如上可简写
j = json.dumps(u, default=lambda obj: obj.__dict__)
print(j)


# json的对象反序列化
def dict2user(d):
    return User(d['name'], d['age'])


u = json.loads(j, object_hook=dict2user)
print(u.name)
