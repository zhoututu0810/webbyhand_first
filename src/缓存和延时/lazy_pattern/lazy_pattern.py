# 设计模式用到了普通类的__new__方法，并且还用到了一个异类的用法
# 我们知道__new__方法返回一个实例对象，它不但可以返回当前类的实例，还能返回一个自定义的实例，看
class Person(object):
    def __init__(self, work, age):
        self.work = work
        self.age = age


class Dog(object):
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return Person('it', age=35)     # 根本不会调用Dog的init  LazyProxy(cls, *args, **kwargs)
        # return super().__new__(cls)

    def __init__(self, dog_name):
        print('init self', self)
        self.dog_name = dog_name


Dog('小白')

# #####################################################
# coding: utf-8
# 请把lazy翻译为"延时"
# 延时代理 本质还是利用缓存，这里很巧妙的利用dict作为缓存，太巧妙了啊。。
class LazyProxy(object):

    def __init__(self, cls, *args, **kwargs):

        self.__dict__['_cls'] = cls
        self.__dict__['_params'] = args
        self.__dict__['_kwargs'] = kwargs

        self.__dict__["_obj"] = None

    def __getattr__(self, item):
        print('Enter LazyProxy getattr')
        if self.__dict__['_obj'] is None:
            self._init_obj()

        return getattr(self.__dict__['_obj'], item)

    def __setattr__(self, key, value):
        print('Enter LazyProxy setattr')
        if self.__dict__['_obj'] is None:
            self._init_obj()

        setattr(self.__dict__['_obj'], key, value)

    def _init_obj(self):
        print('Enter LazyProxy init_obj')
        self.__dict__['_obj'] = object.__new__(self.__dict__['_cls'])
        self.__dict__['_obj'].__init__(*self.__dict__['_params'], **self.__dict__['_kwargs'])


class LazyInit(object):

    def __new__(cls, *args, **kwargs):
        print('enter lazyinit new')
        print(cls)  # 这个为什么是A, 这个是最终要创建的实例的类，屁，因为我调动的是A(1)
        print(args)
        print(kwargs)
        return LazyProxy(cls, *args, **kwargs)


class A(LazyInit):

    def __init__(self, x):
        print("Init A")     # 为什么这里又能够走到这一步呢，在new中返回的不是这个类啊， 因为这一步不是在new后面自动调用的，
        # 而是在LazyProxy中的_init_obj调用的，不信你把LazyProxy的除init方法都注释掉，发现就不会调用了
        print(self)         # <__main__.A object at 0x10dc8c1d0>, LazyProxy对象到哪里去了？
        self.x = 14 + x

print()
a = A(1)
print(a)    # 注意：此时返回的是<__main__.LazyProxy object at 0x10145c210> ，不是A实例对象
# 在访问属性的时候，才实例化，太牛逼了。
# print(a.x)

