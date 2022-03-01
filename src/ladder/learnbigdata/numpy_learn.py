import numpy as np

# arange方法生成连续数字的数组
a = np.arange(24)
print(a)
print(type(a))      # np.arange方法返回一个一维数组, 注意是左闭右开
print(a.ndim, a.shape)  # 1 (15,)  注意一维数据的shape表示方法
print()
a2 = a.reshape(4, 6)     # shapge方法参数是一个shape，重新生成数组的形状，改变原来的数组，生成一个新的数据,这里说的数组就是多维数组
print(a2)
print(a2.shape)      # 显示多维数组的形状
print(a2.ndim)       # 显示多维数组的维度，准确的说是轴数
print(a.size)       # 范湖元素的总个数
print()
a3= a.reshape(2, 3, 4)
print(a3)
print(a3.size, a3.ndim, a3.shape)

# arrage构造函数
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

# 创建数据对象 - 1
# 用标准的Python列表或者元组作为参数，此时，数组的数据类型将根据序列中元素的类型推导出来。
a = np.array([2,3,4])
b = np.array([(1.5,2,3), (4,5,6)])

# 创建初始化数据类型 - 2
# 很多时候，数组的元素最初都是未知的，但其大小形状是已知的。因此，numpy提供了几个函数来创建带有初始占位符内容的数组
# 其他数据类型是创建空对象，numpy不一样，是创建占位符的对象
a4 = np.zeros((5,), dtype = np.float)    # 形状shape参数的单维度写法，tuple的写法，单个数字要写逗号；
a5 = np.zeros((3, 4))
a6 = np.ones( (2,3,4), dtype=np.int16 )                # 同样可以指定类型
a7 = np.empty( (2,3) )   # 根据当前内存状态的不同，可能会返回未初始化的垃圾数值，不安全。
a8 = np.full((3,4), 2.22) # 创建一个全部由2.22组成的数组
a7 = np.random.random((2, 3))
print(a7)