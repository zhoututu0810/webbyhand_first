# 需要将迭代器和生成器做成实用的工具(怎么才是实用的巩固)
from _collections_abc import Iterable
from _collections_abc import Iterator   # class Iterator(Iterable):
from _collections_abc import Generator  # class Generator(Iterator):

from inspect import getgeneratorstate   # 生成器状态
# 可迭代对象可以用for...in...遍历， 本质是该对象内有一个iter方法，该方法返回一个迭代器！当我们使用for循环时，解释器会调用内置的iter()函数
# 迭代器继承自可迭代对象，所以迭代器也是可迭代对象；与众不同的是，迭代器必须实现__next__方法，就可以被next函数作用，有2种遍历方式；
# 生成器继承自可迭代对象，所以前者有的它都有；它还send,throw方法

# #######################################
# 理解yield
# #######################################
def work():
    num = 0
    res = 0
    while True:
        num = yield res     # yield 类似 return，会返回结果，但同时会中断生生成器
        print("receive: ", num)
        res += num
        print("ready to send result: ", res)


w = work()
print(getgeneratorstate(w))     # GEN_CREATED
w.send(None) # 激活生成器  , 等价于 next(w)
# next(w)	# next()方法的本质是调用对象中的
# w.__next__()
print(getgeneratorstate(w))     # GEN_SUSPENDED
print('receive result: ', w.send(1))
print('receive result: ', w.send(2))
print('receive result: ', w.send(3))
print(getgeneratorstate(w))     # GEN_SUSPENDED
w.close()       # GEN_CLOSED
print(getgeneratorstate(w))

print('###########################################')

# #######################################
# 理解yield from
# #######################################
# 理解yield from 的最好的例子
print(isinstance(range(10), Iterable))  # 判断一个对象是否可以迭代
def gen1(iterable):
    yield iterable


def gen2(iterable):
    yield from iterable


g1 = gen1(range(10))
print(isinstance(g1, Generator))    # 判断一个对象是否是生成器 True
for v in g1:    # 为什么遍历不了呢? 遍历的本质是return yield关键字后面的值，gen1返回的就是参数啊
    print(v)

g2 = gen2(range(10))
print(isinstance(g2, Generator))    # 判断一个对象是否是生成器 True
for v in g2:  # 为什么这个可以遍历呢？
    print(v)

