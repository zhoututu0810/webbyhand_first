import itertools
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017783145987360
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。


# itertools.count(start, step)
# class count(object):
#     """
#     count(start=0, step=1) --> count object
#
#     Return a count object whose .__next__() method returns consecutive连续不断的 values.
#     Equivalent to:
#
#         def count(firstval=0, step=1):
#             x = firstval
#             while 1:
#                 yield x
#                 x += step
#     """


# class takewhile(object):
#     """
#     predicate: 断言函数，判断函数
#     takewhile(predicate, iterable) --> takewhile object
#
#     Return successive entries from an iterable as long as the
#     predicate evaluates to true for each entry.
#     """

# 无限序列 + 条件终止
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(type(ns), ns)
list(ns)


# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# 问题，会去重吗？ 不会啊，列表允许重复
for c in itertools.chain('ABC', 'XYZA'):
    print(c)


