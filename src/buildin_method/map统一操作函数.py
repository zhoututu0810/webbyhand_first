# map操作字典
dict1 = {'a': 1, 'b': 2}
# 错误的写法，返回的是 [2, 3], map返回的集合是处理函数func返回的结果的集合，这一点和sorted和filter有本质的区别，sorted和filter都是原来的
# 集合元素根据判断是否调换顺序或者保留，最后的集合还是原来元素的集合。
print(list(map(lambda x: x[1]+1, dict1.items())))   # [2, 3]

# 正确的写法
print(dict(list(map(lambda x: (x[0], x[1]+1), dict1.items()))))   # [('a', 2), ('b', 3)]
