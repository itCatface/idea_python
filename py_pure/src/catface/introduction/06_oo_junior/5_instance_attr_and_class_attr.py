# -实例属性&类属性[千万不要对实例属性和类属性使用相同的名字]
class Person(object):
    name = 'Person'

    def __init__(self):
        pass


p = Person()
print("p's name:", p.name)
print("Person's name:", Person.name)
p.name = 'ashe'
print("p's name:", p.name)
print("Person's name:", Person.name)
del p.name
print("p's name:", p.name)
print("Person's name:", Person.name)
# p's name: Person
# Person's name: Person
# p's name: ashe
# Person's name: Person
# p's name: Person
# Person's name: Person
