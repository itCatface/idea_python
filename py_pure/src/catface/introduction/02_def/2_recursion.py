# -递归函数


# 阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# print(fact5))          # 120
# 计算过程示例如下
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120


# 函数是通过栈实现的，没进入一个函数调用，就会增加一层栈，当函数返回，就会减少一层栈，当递归次数过多会导致栈溢出
# 尾递归即函数返回时调用自身本身，且return语句不能包含表达式，使得递归无论调用多少次都只占用一个栈，不会出现栈溢出
# 注意：尾递归如果做了优化，栈就不会增长，但是大多数语言都没针对尾递归做优化，包括python，所以及时此处使用了尾递归，也会导致栈溢出
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, result):
    if 1 == num:
        return result
    return fact_iter(num - 1, num * result)


print(fact2(5))


# 幂
def _32(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

# print(_32(3, 3))               # 27
