# https://www.liujiangblog.com/course/data/219
# Series 可以读作串，可以看做是 ：可以自定义索引的一维索引
# Series是一个一维的数组对象，它包含一个值序列和一个对应的索引序列
# Numpy的一维数组通过隐式定义的整数索引获取元素值，而Series用一种显式定义的索引与元素关联
# 显式索引让Series对象拥有更强的能力，索引也不再仅仅是整数，还可以是别的类型，比如字符串，索引也不需要连续，也可以重复，自由度非常高。

import pandas as pd

# 使用Series构造器构造串,data参数可以是列表，也可以是元祖
# index是索引，不指定的时候默认和list一样哦！
# def __init__(self, data=None, index=None, dtype=None, name=None, copy=False, fastpath=False):
s1 = pd.Series([1, -1, 2, 4])
# s1 = pd.Series((3, 4, 7, 3))  # 可以是列表，也可以是元祖
s2 = pd.Series([7,-3,4,-2], index=['d','b','a','c']) # 创建的时候指定索引，索引是一个列表
s3 = pd.Series(5, index=list('abcde'))  # 根据索引补充数据, data可以是数字，列表，或者以为数组
s4 = pd.Series({2:'a',1:'b',3:'c'}, index=[3,2]) # 通过index筛选结果, 通过字典构建Series, key是索引，value是值
print(s1.dtype)     # int64
print(s1.index)     # 返回一个索引对象 RangeIndex(start=0, stop=4, step=1)对象，左闭右开！！
print(issubclass(pd.RangeIndex, list))  # False
print(type(s1.values), s1.values) # 返回的numpy数组 <class 'numpy.ndarray'> [ 1 -1  2  4]

#
# 操作：修改索引
#
s1.index = ['a','b','c','d']    # 给RangeIndex对象赋值，就可以修改索引，神奇！

#
# 操作：查询
#
print(s1[0])   # 类似list,通过索引获取value
print(s1[[1, 2]])   # 为了方便，还可以传递一个索引列表，一次获取多个值哦！


# 创建Series时候指定索引
s2 = pd.Series([7, -3, 4, -2], index=['d', 'b', 'a', 'c'])  # index初始化参数也是一个列表
print(s2.index)     # 返回一个Index对象：Index(['d', 'b', 'a', 'c'], dtype='object')

# 根据索引补充数据
s3 = pd.Series(5, index=list('abcde'))

# 通过字典构建Series,默认用键作索引，如果制定了索引餐宿index，则会根据index中的索引值去过滤字典哦！
s4 = pd.Series({'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000})
s5 = pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])   # 通过index筛选结果
print('shanghai' in s4)     # in操作类似字典哦！判断的是索引是否存在，不是值是否存在
print(s4.item())        # 类似字典，返回的是包含(key, value)对的zip对象，可以通过list迭代
print(list(s4.item()))


# 空值情况
dic = {'beijing':35000,'shanghai':71000,'guangzhou':16000,'shenzhen':5000}
city = ['nanjing', 'shanghai','guangzhou','beijing']
s7=pd.Series(dic, index=city)

# 应用
# 1
print(s2[s2>0])     # 单个筛选条件，有多个筛选条件吗？
# 2
# 3



