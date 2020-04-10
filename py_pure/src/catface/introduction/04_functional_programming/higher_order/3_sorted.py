# -排序算法
l = [3, 34, -23, 4, -34, -12, 53, 8, -34]
print(sorted(l))

print(sorted(l, key=abs))

print(sorted(l, reverse=True))

# 按ASCII码排序
names = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(names))

print(sorted(names, key=str.lower, reverse=True))

# --分别按key/value排序
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(x):
    return x[0]


def by_score(x):
    return x[1]


print(sorted(l, key=by_name))
print(sorted(l, key=by_score))
# 使用lambda，效果同上
print(sorted(l, key=lambda t: t[0]))
print(sorted(l, key=lambda t: t[1]))
