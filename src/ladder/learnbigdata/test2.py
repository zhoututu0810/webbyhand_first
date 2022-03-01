import numpy as np
import pandas as pd

company = ['A', 'B', 'C']
department = ['d1', 'd2', 'd3']
data = pd.DataFrame({
    "company": [company[x] for x in np.random.randint(0, len(company), 10)],
    "department": [department[x] for x in np.random.randint(0, len(department), 10)],
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(20, 40, 10),
})
print(data)
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.values)    # 重要属性， 二维列表

# 看看一维情况
s1 = data['salary']
print(s1)
print(type(s1))  # <class 'pandas.core.series.Series'>
print(s1.values)    # [32 39 28  5 49 33 13 17 38 11]
print(type(s1.values))  # <class 'numpy.ndarray'>
#
print('test head')
print(type(data.head(1)))  # <class 'pandas.core.frame.DataFrame'>
print(data.head(1).values)  # [['A' 'd1' 33 21]]

# 按条件筛选行
print(data['company'] == 'A')
print(type(data['company'] == 'A'))    # <class 'pandas.core.series.Series'>
# 按多条件筛选 |

# 添加列
# data['satus'] = 1
data.loc[:, 'status'] = 1   # loc可以索引不存在的列，达到添加列的效果
print(data)
print(data.apply(lambda x: x.salary + x.age, axis=1))
print(type(data.apply(lambda x: x.salary + x.age, axis=1)))  # <class 'pandas.core.series.Series'>



stp1 = data.groupby(['company', 'department'])
# stp1 = data.groupby(['company'])
print(type(stp1))   # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
print(stp1)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x10b7c7b10>
print(list(stp1))
print()
stp2 = stp1['salary']
print(type(stp2))   # <class 'pandas.core.groupby.generic.SeriesGroupBy'>
print(stp2)  # <pandas.core.groupby.generic.SeriesGroupBy object at 0x11cf19990>
print(list(stp2))
print()
stp3 = stp2.mean()
print(type(stp3))   # <class 'pandas.core.series.Series'>
print(stp3)
print(stp3.name)    # salary
print(stp3.index)  # Index(['A', 'B', 'C'], dtype='object', name='company')  # 串名是列名，索引名是分组名
print()
print(stp3.to_dict())   # {'A': 32.0, 'B': 32.5, 'C': 32.0}
print()
stp4 = stp3.reset_index()
print(stp3.reset_index())


