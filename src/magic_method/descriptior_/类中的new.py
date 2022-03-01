class A(object):  # -> don t forget the object specified as base

    def __new__(cls):
        print("A.__new__ called")
        # print(cls)        # A
        # print(type(cls))    # type
        # print(super(A, cls) is type)  # false
        # print(super(A, cls) is object)  # false
        return super().__new__(cls)

    def __init__(self):
        print("A.__init__ called")


print(hasattr(type, '__new__')) # Ture
print(hasattr(object, '__new__'))   # Ture
a = A()
