class base(object):
    __slots__ = ('x')
    var = 8

    def __init__(self):
        pass


b = base()
b.x = 88  # 添加实例变量
print(b.x)
print(b.var)
# b.y=99    # 无法动态添加slot之外的属性
# print(b.__dict__)     # 无法创建__diect__

