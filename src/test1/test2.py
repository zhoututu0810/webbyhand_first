from collections.abc import Iterable, Iterator
map_result = map(lambda x: x+1, [1, 2])
print(list(map_result))     # [2, 3]
print(list(map_result))     # []
print(isinstance(map_result, Iterator))     # True  map既是迭代器，也是可迭代对象

rg_a = range(5)        # range是可迭代对象，但不是一个迭代器
print(isinstance(rg_a, Iterator))      # False
print(isinstance(rg_a, Iterable))      # True