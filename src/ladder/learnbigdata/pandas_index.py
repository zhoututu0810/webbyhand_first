# Pandas中的索引对象Index()用于存储轴标签（可以理解为某个方向行或列的标记，比如哪一行，那一列）和其它元数据。\
# 索引对象是不可变的，用户无法修改它，但是pandas对象可以重建索引。
import numpy as np
import pandas as pd

s1 = pd.Series(range(3),index = ['a','b','c'])
index = s1.index
print(type(index))  # 是一个索引Index对象，<class 'pandas.core.indexes.base.Index'>
print(index)    # Index(['a', 'b', 'c'], dtype='object')
print('---------注意：这个是切片S1-----------')
print(s1[1:])       # <class 'pandas.core.series.Series'>
print(type(s1[1:])) # 切片后返回一个新的对象，返回新的对象的数据类型和原来的一样，合理！
print(s1)           # 切片不影响原来的对象
print('---------注意：下面的才是切片索引-------')
print(index[1:])        # Index(['b', 'c'], dtype='object')
print(type(index[1:]))  # 切片后返回一个新的对象，返回新的对象的数据类型和原来的一样，合理！
print(index)            # 切片不影响原来的对象


# 构建索引
#    def __new__(
#         cls, data=None, dtype=None, copy=False, name=None, tupleize_cols=True, **kwargs,
#     ) -> "Index":
labels = pd.Index(np.arange(3))
s1 = pd.Series([2,3.5,0], index=labels) # 这种索引赋值哦，神奇吧！

