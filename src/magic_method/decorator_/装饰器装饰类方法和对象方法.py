# 之前讲的都是装饰普通的函数，而不是方法
# 总结：函数装饰器可以装饰 对象方法和类方法，装饰类方法，装饰器函数要写在里层；
#      类装饰器，不能装饰类对象和类方法，
def decorator(func):
    print('外层内容1')

    def wrapper(*args, **kwargs):
        print('内部功能')
        func(*args, **kwargs)

    return wrapper


# 假如是一个类装饰器呢？
class DecraotorClass(object):
    def __init__(self, function):
        print('init')
        self.function = function

    def __call__(self, *args, **kwargs):
        print('call')
        print(*args)
        print(**kwargs)
        self.function(*args, **kwargs)


class Animal(object):
    def __init__(self, age, color):
        self.age = age
        self.color = color

    @decorator
    def eat(self):  # 变成了 eat = wrapper = decorator(eat)
        print('eat')

    @decorator
    def bark(self, a):
        print('bark', a)

    @classmethod
    @decorator  # 为什么这个要写在下面。这个只是简单的函数执行。返回的也是一个方法。把心的函数变成类方法。
    def func(cls):
        print('cls')

    @DecraotorClass
    def func2(self):    # func2 = DecraotorClass(func2) 是一个对象，对象()，没见过这种用法
        print('func2')


print('还没开始呢就有打印了')  # 装饰器再书写的时候就调用了
# print('测试函数装饰器装饰对象方法')
# a = Animal(5, 'rad')
# a.eat()     # 调用eat = wrapper，函数参数一样
# print()
# a.bark('aaa')
# print('测试调用类方法')
# Animal.func()

print('类装饰器装饰对象方法')
a = Animal(5, 'rea')
a.func2()       # 想象为什么报错。

