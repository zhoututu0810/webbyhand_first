import numpy as np
import pandas as pd
a1 = np.random.randint(5, size=(5,))
print(a1)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=list('abcd'))
print(df1)
print(df1['a'])
print(type(df1['b']))
print(df1['a'][1])

print(df1.iloc[1])  # 单个索引值得时候检索的是行
# print(df1.loc['a'])     # 报错
print(df1.iloc[0:1])      # 这个不会降维，我勒个去
print(type(df1.iloc[0:1]))

# df2 = df1.loc[0:2, 'a':'b']
# print(df2)
# df2[:] = 10
# # df2.reshape((3,2 )) # 问题df对象如何改变形状？？
# print(df2)
# print(df1)

# a= np.arange(12).reshape((3, 4))
# print(a)
# b = a[:,0:2]
# print(b)
# b[:]=10
# print(b)
# print(a)

# a2 = np.arange(12).reshape((3, 4))
# print(a2)
# b = [0, 2]
# print(a2[b])
#
# print()
# df3 = pd.DataFrame(np.random.randint(0, 10, (5, 4)), columns=list('ABCD'))
# print(df3[:]['B']   )