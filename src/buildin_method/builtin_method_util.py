# (1) 5星，非常有用和方便
# zip 按位置取， 数据结构为：必须要记住 二元列表-元祖 [(),(),()]
# 使用场景：多个可迭代对象，按位置取数
# https://www.runoob.com/python/python-func-zip.html
from collections.abc import Generator
from collections.abc import Iterator
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = zip(a, b)
print(zipped)    # <zip object at 0x107917410>
print(type(zipped))  # <class 'zip'>
print(isinstance(zipped, Generator))     # False
print(isinstance(zipped, Iterator))      # True
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print()

# *zipped，也是按位置取，厉害吧. 搞不懂！
zip(*zipped)

# (2)



# (3)


# (4)