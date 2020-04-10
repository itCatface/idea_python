# encoding=utf-8

import numpy as np

from numpy.linalg import *


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))

    np_list = np.array(lst)
    print(type(np_list))

    # 1. 指定数组唯一类型
    np_list = np.array(lst, dtype=np.float)

    print(np_list.shape)  # 行数列数
    print(np_list.ndim)  # 维度
    print(np_list.dtype)  # float64
    print(np_list.itemsize)  # 8
    print(np_list.size)  # 6

    # 2. 一些数组
    print(np.zeros([3, 5]))
    print(np.ones([2, 3]))
    print("random:")
    print(np.random.rand(2, 4))  # 0-1的随机数
    print(np.random.rand())
    print("random int:")
    print(np.random.randint(1, 10))
    print(np.random.randint(1, 15, 4))
    print("randn:")  # 标准正态分布？均匀分布？
    print(np.random.randn(2, 4))
    print("choice:")
    print(np.random.choice([1, 3, 5]))
    print("distribute:")  # 数学中的各种分布
    print(np.random.beta(1, 10, 100))

    # 3. 一些操作
    print(np.arange(1, 15))  # 等差数列
    print(np.arange(1, 10).reshape([3, 3]))
    print(np.arange(1, 10).reshape([3, -1]))  # -1是缺省

    lst = np.arange(1, 10).reshape([3, -1])
    print("exp:")
    print(np.exp(lst))
    print("exp2:")
    print(np.exp2(lst))
    print("sqrt:")
    print(np.sqrt(lst))
    print("sin:")
    print(np.sin(lst))
    print("log:")
    print(np.log(lst))

    # 求和
    lst = np.array([[[1, 3, 5],
                     [2, 4, 6]],
                    [[9, 8, 7],
                     [3, 5, 4]],
                    [[19, 5, 12],
                     [3, 21, 7]]])

    print("sum is:", lst.sum(), "max is:", lst.max(), "min is:", lst.min())

    print("axis=0:")
    print(lst.sum(axis=0))  # 只对最外层操作
    print("axis=1:")
    print(lst.sum(axis=1))
    print("axis=2:")
    print(lst.sum(axis=2))
    print("max axis=1:")
    print(lst.max(axis=1))
    print("min axis=1:")
    print(lst.min(axis=1))

    lst1 = np.array([1, 3, 5, 7])
    lst2 = np.array([2, 4, 6, 8])
    print("add:")
    print(lst1 + lst2)
    print("sub:")
    print(lst1 - lst2)
    print("mul:")
    print(lst1 * lst2)
    print("div:")
    print(lst1 / lst2)
    print("square:")
    print(lst1 ** lst2)
    print("矩阵乘法:")
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))

    print("追加:")
    print(np.concatenate((lst1, lst2), axis=0))
    print("上下追加:")
    print(np.vstack((lst1, lst2)))
    print("追加:")
    print(np.hstack((lst1, lst2)))
    print("切割:")
    print(np.split(lst1, 2))
    print("拷贝数组:")
    print(np.copy(lst1))

    # 4. 线性方程组和矩阵运算
    print("单位向量:")
    print(np.eye(4))
    lst = np.array([[1, 2], [3, 4]])
    print("逆:")
    print(inv(lst))
    print("T:")
    print(lst.transpose())
    print("单位向量和特征值:")
    print(det(lst))
    print(eig(lst))

    print("解方程:")
    y = np.array([[5.], [7.]])
    print(solve(lst, y))

    # 5. other
    print("fft:")
    print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1])))
    print("corrcoef:")
    print(np.corrcoef([1, 0, 1], [0, 1, 3]))
    print("poly:")
    print(np.poly1d([2, 1, 3]))


if __name__ == '__main__':
    main()
