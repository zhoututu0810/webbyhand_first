# https://www.liujiangblog.com/course/data/220
# df就是一个二维的excel表或者数据库的table
# 每一列可以是不同的值类型(类似数据库或者Excel表头,所以列索引一般都有实际意义)
# DataFrame既有行索引，也有列索引(excel的列索引是A,B,C, 行索引是1,2,4..   数据库的列索引就是字段名，行索引就是行数1,2,3)
import numpy as np
import pandas as pd

#修改最大显示行和列

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)

# DataFrame构造函数
# def __init__(self,data=None,index: Optional[Axes] = None,columns: Optional[Axes] = None,
#              dtype: Optional[Dtype] = None,copy: bool = False,):

# 构造方法 - 用字典构造
# 每一列可以看多是一个字典，key是列名，value是列的值得序列
data = {'state': ['beijing', 'beijing', 'beijing', 'shanghai', 'shanghai', 'shanghai'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2
                ]}

df1 = pd.DataFrame(data=data)
df1 = pd.DataFrame(data=data, columns=['year','state','pop']) # columns就是列索引，这样会指定列排序，不是筛选哦！
df1 = pd.DataFrame(data=data, columns=['year','state','pop'], index=list('abcdef'))
print(df1)
print(df1.columns)  # 返回索引对象 Index(['state', 'year', 'pop'], dtype='object')'
# RangeIndex(start=0, stop=6, step=1) 是默认索引，如果指定了索引，就会返回Index对象
print(df1.index)    # 返回索引对象 Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
print(type(df1.values))     # 注意：返回的np的数组对象 <class 'numpy.ndarray'>
print(df1.values)   # 查看数据，不包括索引
print()
print('test------')
aa = df1.loc['b':'c', 'year':'state']
print(df1)
print(aa)

# #########################
# 数据新增
# #########################
# 1.追加列
df1['debt_1'] = 12        # 类似字典操作，把每一个列看做一个字典
df1['debt_2'] = np.arange(1,7)  # 可是是n维数组对象
df1['debt_3'] = [2,4,1,2,5,6]   # 可是是序列
s1 = pd.Series([1,2,3],index = ['c','d','f'])
df1['debt_4'] = s1      # 可以是Series对象，注意: 缺失值以NaN填补
print(df1)
# 2.追加行
df2 = df1.loc['b']
df1.append(df2)         # 类似列表的操作


# #########################
# 创建7中方式
# https://blog.csdn.net/sxb0841901116/article/details/91044401
# #########################
# merge合并重名问题
df1 = pd.DataFrame(data={
        'name':['xiaoming', 'zhangsan', 'wangpangzi'],
        'age': ['13', '14', '15'],
        'field1': ['aa1', 'aa2', 'aa3']
})
print(df1)
df2 = pd.DataFrame(data={
        'name':['xiaoming', 'zhangsan'],
        'sex': ['1', '0'],
        'field1': ['bb1', 'bb2']
})
print(df2)
print(df1.merge(df2, how='left', on='name'))
