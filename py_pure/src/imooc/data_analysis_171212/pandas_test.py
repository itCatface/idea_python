import datetime

import numpy as np
import pandas as pd
from pylab import *
import xlrd


def main():
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(type(s))
    dates = pd.date_range('20171213', periods=8)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list('ABCDE'))
    print(df)

    df1 = pd.DataFrame({'A': 1, 'B': pd.Timestamp('20171213'), 'C': pd.Series(1, index=list(range(4)), dtype='float'),
                        'D': np.array([3] * 4, dtype='float32'),
                        'E': pd.Categorical(['police', 'student', 'teacher', 'doctor'])})
    print(df1)

    # 1.基本操作
    print(df.head(3))
    print(df.tail(3))
    print(df.index)
    print(df.values)
    print(df.T)
    print(df.sort_values('C'))
    print(df.sort_index(axis=1, ascending=False))
    print(df.describe())

    # 2.切片[key&index]
    print(df['A'])
    print(type(df['A']))
    print(df[:3])
    print(df['20171214':'20171215'])
    print(df.loc[dates[0]])
    print(df.loc['20171214':'20171216', ['B', 'D']])
    print(df.at[dates[0], 'C'])

    print(df.iloc[1:3, 2:4])
    print(df.iloc([1, 4]))
    print(df.iat[1, 4])

    print(df[df.B > 0][df.A < 0])
    print(df[df > 0])
    print(df[df['E'].isin([1, 2])])

    # 3. 设置
    s1 = pd.Series(list(range(10, 18)), index=pd.date_range('20171213', periods=8))
    df['F'] = s1
    print(df)
    df.at[dates[0], 'A'] = 0
    print(df)
    df.iat[1, 1] = 1
    df.loc[:, 'D'] = np.array([4] * len(df))
    print(df)

    df2 = df.copy()
    df2[df2 > 1.0] = -df2
    print(df2)

    # 4.缺失值处理
    df3 = df.reindex(index=dates[:4], columns=list('ABCD') + ['P'])
    df3.loc[dates[0]:dates[1], 'Y'] = 1
    print(df3)
    print(df3.dropna())
    print(df3.fillna(value=2))

    # 5.表格、形状
    print(df.mean())
    print(df.var())
    s = pd.Series([1, 2, 2, np.nan, 5, 7, 9, 10], index=dates)
    print('s is:\n', s)
    print(s.shift(2))  # 所有值往后移
    print(s.diff())  # 后面减前一位
    print(s.value_counts())

    print(df.apply(np.cumsum))
    print(df.apply(lambda x: x.max() - x.min()))

    # 拼接
    pieces = [df[:3], df[-3:]]
    print(pd.concat(pieces))
    left = pd.DataFrame({"key": ['x', 'y'], 'value': [1, 2]})
    right = pd.DataFrame({"key": ['x', 'z'], 'value': [3, 4]})
    print('left:', left)
    print('right:', right)
    print(pd.merge(left, right, on='key', how='inner'))
    print(pd.merge(left, right, on='key', how='outer'))
    print(pd.merge(left, right, on='key', how='left'))

    df3 = pd.DataFrame({'A': ['a', 'b', 'c', 'b'], 'B': list(range(4))})
    print(df3.groupby('A').sum())

    # reshape[数据的交叉分析中常用]
    df4 = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                        'B': ['a', 'b', 'c'] * 8,
                        'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                        'D': np.random.randn(24),
                        'E': np.random.randn(24),
                        'F': [datetime.datetime(2017, i, 1) for i in range(1, 13)] +
                             [datetime.datetime(2017, i, 15) for i in range(1, 13)]})
    print(pd.pivot_table(df4, values='D', index=['A', 'B'], columns=['C']))

    # 时间序列
    t_exam = pd.date_range('20171213', periods=10, freq='S')
    print(t_exam)

    # 绘图
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('20171213', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    show()

    # 文件操作
    df6 = pd.read_csv('data/test.csv')
    print(df6)
    df6.to_csv('data/test_copy.csv')
    df7 = pd.read_excel('data/test.xls', 'Sheet1')
    print(df7)


if __name__ == '__main__':
    print(xlrd.__VERSION__)
    main()
