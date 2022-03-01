# 单独开一章将布尔索引
# 布尔索引分2类，一类是和待检索数据结构一样，一类是和待检索数据的某个轴结构一样
import numpy as np
import pandas as pd

# 第一个类，和元数据索引结构一致，很好理解，
# 适用于赋值操作
a1 = np.arange(12).reshape(3, 4)
b = a1 > 4   # 获取布尔数据
a1[b] = 0
# 可以简化为 a[a>4] = 0
# a[~(a>4)] = 0
# a[(a>4) & (a<6)] = 0
# a[(a<4) | (a>6)] = 0
print()

# numpy的多维数据索引操作符[]默认就是支持行和列索引，pandas中的多维数据DF就不行，默认只支持列索引，
# DataFrame如果需要行列索引，需要用到loc函数
# arange[行切片，列切片], 如果哪个轴确实，那个轴相当于全选
a2 = np.arange(12).reshape(3, 4)
# array[行索引，列索引]
print(a2)
print(a2[2, 3])     # 第3行第4列的元素，注意索引从0开始计数
print(a2[2][3])     # 同上
print(a2[0:2, 3])   # 选择第0, 1行，第4列
print(a2[0:2])      # 选择第0, 1行，却是列就是所有列
print(a2[0:2, :])   # : 全选
print('测试数组索引')
# 有了上面的只是，要先看数组索引，才好理解布尔索引
i = np.array([0, 1])
j = np.array([0, 1, 2, 3])
print(a2[0:2])
print(a2[i])    # 同比上面的规则，第一个位置标示筛选行，和切片一样啊
print()
# print(a2[0:2, : ])
# print(a2[i, j]) # 报错！！这个就是一个坑了，如果是多个数组索引做参数，它分别取的i和j同位置组成一个索引，再去原数据取值
print()
print(a2[0:2, 3])
print(a2[i, 3])    # 这个也是反人类的，拿i中的数和3拼接成一个索引值，再去原数组拿数, 这个虽然反人类，但是效果一样
print('测试布尔索引')
# 有了上面的只是，我们再来看看 "布尔索引"
b1 = np.array([False, True, True])
b2 = np.array([True, False, True, True])
k = np.array([1, 2])
v = np.array([0, 2, 3])
print(a2[k])
print(a2[b1])   # 只拿True的行，False的忽略
print()
print(a2[k, 1:2])
print(a2[b1, 1:2])
print()
# print(a2[k, v])
# print(a2[b1, b2])    # 和上面的报错一样
# 切片只能连续筛选，布尔可以离散实现，很显然离散筛选作用更啊，连续的常见很少

# 我们再来看看DF的例子
df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['l0', 'l1', 'l2'], columns=list('abcd'))
print(df1)
# 在DataFrame中，索引检索操作符[] 默认按列操作，但是切片默认按行操作！
print(df1['b'])
# print(df1['a', 'b'])      # 报错，不支持行列模式
print(df1[['a', 'b']])      # 注意数组是这么写，不要写成行列2个参数模式了
# print(df1['a': 'b'])      # 报错，切片模式似按行索引
print('测试索引符号+布尔数组')
# i = np.array([True])      # 报错，布尔索引必须和检索的行或者列的索引长度一致
i = np.array([True, False, True])   # dtype: bool, 数据类型真的是bool哦，
idx = df1['a'] > 3      # 布尔索引默认是筛选行哦,和切片一样，列要满足啥条件，就把它当做sql来思考
print(idx)
print(df1[i])
print()
print(df1[0:2])             # 选择第一行，第二行
print(df1['l0': 'l1'])      # 字母索引的显式索引同样支持切片，并且显示索引左右双闭，隐式索引左闭右开
print()
# 注意loc只能用显示索引，iloc只能用隐式索引，最最推荐的就是loc方法了
print('loc数组索引 - 离散取值')
print(df1.loc['l0'])
print(df1.loc[['l0', 'l1']])
print(df1.loc['l0', 'a'])   # 获得单个值
print(df1.loc[['l0', 'l1'], ['a', 'b']])
print('loc切片索引 - 连续取值')
# print(df1.loc[0:2])       # 报错，用了隐式索引
print(df1.loc['l0':' l1'])  # 显示索引，左右双闭
print(df1.loc['l0': 'l1', : ])
print(df1.loc['l0': 'l1', 'a':'d'])
print()
print(df1.iloc[0:2])
print(df1.iloc[0:2, :])
print(df1.iloc[0:2, 0:4])   # 隐式索引，左闭右开
print('测试布尔索引')
# i = np.array([True, False]) # 报错，长度不够
# 如何理解i? i是一个布尔索引，不是行索引也不是列索引，看它用的位置，如果放在loc的第一个位置，表示行索引，海选行，那么索引长度
# 必须和行索引长度一致，最快速的获取和行索引成都一致的索引就是取某个列的数据了，df['a'] > 1,获取某一个列的数据，长度肯定和行的
# 索引长度一样
i = np.array([True, False, True])
print(df1.loc[i])
print(df1.loc[i, :])
print(df1.loc[i, 'a'])
# j也只是一个布尔数组，放在loc的第二个参数位置，表示要筛选列，那么要和列的索引产股一致，因为df[]只能筛选列，所以要获取和列索引
# 长度一致的布尔数据，要用df.loc['l0'] > 2, 也很方便！！
j = np.array([True, True, False, False])
print(df1.loc[:,j])
# print(df1.iloc[i])
# 求第三列大于4的所有行
# 分析：最终是要筛选行，那么要loc的第一个位置，过滤行索引
print(df1.loc[(df1['c'] > 4)])
# 求第三列大于4的所有行，某些列
print(df1.loc[(df1['c'] > 4), ['a', 'b']])
# 求第三列大于4且小于8的所有行
print(df1.loc[(df1['c'] > 4) & (df1['c'] < 8)])
# 求第三列大于4，第四列==11的所有行
print(df1.loc[(df1['c'] > 4) & (df1['d'] == 11)])

print()
print('测试any')
# any 和 python的any函数类似
df2 = pd.DataFrame(np.random.randn(1000, 4))
print(df2)
print(df2 > 3)
print(df2[df2 > 1])     # 这个全结构的布尔索引和numpy的数组不一样哦，这里没有降维
print((df2 > 1).any(1)) # 1表示列轴方向，就是左右方向，操作
df2[df2 > 1] = 0
print(df2)