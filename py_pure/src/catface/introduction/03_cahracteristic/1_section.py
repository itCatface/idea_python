# -切片->list | tuple
names = ['tom', 'bob', 'ivan', 'kin', 'catface']
print(names[:])  # ['tom', 'bob', 'ivan', 'kin', 'catface']
print(names[0:3])  # ['tom', 'bob', 'ivan']
print(names[:3])  # ['tom', 'bob', 'ivan']    # 第一个索引是0，则可以省略
print(names[1:3])  # ['bob', 'ivan']
print(names[1:6])  # ['bob', 'ivan', 'kin', 'catface']

print(names[-3])  # ivan
print(names[-3:-1])  # ['ivan', 'kin']
print(names[-3:0])  # []
print(names[-3:])  # ['ivan', 'kin', 'catface']

nums = list(range(7))
print(nums)  # [0, 1, 2, 3, 4, 5, 6]
print(nums[1::2])  # [1, 3, 5]         #  从第一个数开始，每两个取一个
print(nums[:5:2])  # [0, 2, 4]         # 前五个数，每两个取一个
print(nums[::-2])  # [6, 4, 2, 0]
print(nums[::2])  # [0, 2, 4, 6]

# tuple和字符串操作是一样一样的
s = 'abcdefg'
print(s[-5:-1])  # cdef
for char in s[1::2]:
    print(char)
