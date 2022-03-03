# 字典过滤
dict1 = {'a': 1, 'b': 2}
def func_filter(x):
    print(x[1])
    if x[1] >= 2:
        return False    # 错误的写法
    # 注意上面这种错误的写法，filter函数只保留ture的item，但是上面的写法是返回了false，最后到时过滤的结果是空的
    # 应该这么写
    if x[1] < 2:
        return True

# print(list(filter(func_filter, dict1)))     # 错误，字典默认遍历的是key，相当于在遍历前执行了dict.keys()方法
print(list(dict1.items()))
print(list(filter(func_filter, dict1.items())))

# 字典过滤结果lambda
dic = {'k1': 10, 'k2': 100, 'k3': 50, 'k4': 90}
print(dict(list(filter(lambda x: x[1] > 50, dic.items()))))  # 把值大于50的由元祖组成的键值对过滤出来。

sum()