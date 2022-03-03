# 字典排序, 字典是没有顺序的，对字典排序是没有意义的，字典的排序要用到有序字典orderdict
dict1 = {'b': 1, 'a': 3}
print(sorted(dict1, key=lambda x: x))   # ['a', 'b']
print(sorted(dict1))    # ['a', 'b']   这两种等价，只能把key提取出来排序，那么怎么对整个字典排序呢？
# 如果要按照值来排序，可以将字段转换换为数组
print(dict1.items())    # dict_items([('b', 1), ('a', 3)])， dict_items可迭代对象
print(dict(dict1.items()))  # 将列表转换为数组，本身字典就提供这种构造方法


# 时间排序