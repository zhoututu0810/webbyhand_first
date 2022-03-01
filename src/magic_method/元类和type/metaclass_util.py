# 将元类用于实战
# 普通方法中的new动态改变对象的属性，因为new返回的是对象，自己创建的类就可以用new
# 元类中的new返回的是new是类，可以改变类属性。元类的好处是，如果别人定义了一个类，但是我又不能修改那个类，但是我有想
# 改变那个类的创建，就用元类劫持，类似yield from 委托代理系统的生成器对象
# 类A的————class--
class A(object):
    pass
class B(A):
    pass
b=B()
print(b.__class__)  # <class '__main__.B'>
print(B.__class__)  # <class 'type'>
print(A.__class__)  # <class 'type'>
print(issubclass(A, A))  # 居然是True的，说明什么？当前类是当前类的子类，是临界用法。记住就好

print()

# 普通类中的————new
class Person(object):
    def __init__(self, name, age):
        print('enter init')
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('enter new')
        print(cls)      # <class '__main__.Person'>
        print(id(cls))  # 140312166105056
        print('构造方法 args ->', args)
        print('构造方法 kwargs ->', kwargs)
        print(super())  # <super: <class 'Person'>, <Person object>>，逗号前面的是一个整体
        instance = super().__new__(cls)
        print(instance) # <__main__.Person object at 0x10ad68290>
        print(id(instance)) # 4551627472  返回的是对象
        return instance
print('测试初始化')
p1 = Person('张三', 18)
print(id(Person))   # 140312166105056
print(id(p1))   # 4339417552        # 说明该对象就是new方法犯规的对象哦！

print()

# ### 元类中的--new
# 简单
class BaseClass(type):
    # 注意该方法：每有一个类用了该元类，就会自动调用一次
    def __new__(abc, *args, **kwargs):
  # def __new__(cls, name, bases, attrs_dict):  # 本质是这个方法哦，不是上面一行args的定义
        print("--- enter BaseClass ---")   # <class '__main__.BaseClass'>
        print(abc)  # <class '__main__.BaseClass'>
        print(BaseClass)    # <class '__main__.BaseClass'>
        print(abc.__class__)    # <class 'type'>
        print(__class__)    # <class '__main__.BaseClass'> # 从这个可以判断谁调用这个方法，是User类
        print(args) # ('User', (), {'__module__': '__main__', '__qualname__': 'User', '__init__': <function User.__init__ at 0x10838fb00>})
        print(kwargs)
        print(BaseClass.__class__)  # <class 'type'>
        print(super())  # <super: <class 'BaseClass'>, <BaseClass object>>
        return super().__new__(abc, *args, **kwargs)


class User(metaclass=BaseClass):
    def __init__(self, name):
        self.name = name

print('开始测试元类')
user = User("wangbm")
print('user.__class__', user.__class__) # <class '__main__.User'>
print(User.__class__)   # <class '__main__.BaseClass'>
print(BaseClass.__class__)  # <class 'type'>

print()
# 单层
class NewMetaClass(type):
    def __new__(cls, name, bases, attrs): # name是你要制造成类的名字(类A),bases是类A的父类，attrs是一个字典，放有类A里的属性和方法
        # 不理解这个cls, 为什么是 <class '__main__.NewMetaClass'>
        print(cls)  # <class '__main__.NewMetaClass'>
        print('name', name)
        print('base', bases)
        print('attrs', attrs)
        # cls是元类的对象，没错，找的是元类中的mro
        print(NewMetaClass.__class__)   # <class 'type'>
        print(NewMetaClass.__class__.__mro__)  # (<class 'type'>, <class 'object'>) ???
        print(super()) # <super: <class 'NewMetaClass'>, <NewMetaClass object>>
        print(super(NewMetaClass, cls).__new__(cls, name, bases, attrs))  # (super...) 是A的类对象
        return super(NewMetaClass, cls).__new__(cls, name, bases, attrs)  # return xxx 以后传入self

    def __init__(self, *args, **kwargs):
        # 此self是A的类对象 (另super(NewMetaClass, self).__init__(*args, **kwargs)的值为None)
        super(NewMetaClass, self).__init__(*args, **kwargs)
        print(self)


class A(object, metaclass=NewMetaClass):
    # metaclass = 相当于给该类的__metaclass__赋值
    pass


a = A()
print('A类的mro', a.__class__.__mro__)

print()
# 还是以最简单的动物为例 - 多层
class Animal(object):
    pass


class RunMixin():
    def run(self):
        print('RunMixin: run')
        print('run self:', self)


class BarkMixin():
    def bark(self):
        print('BarkMixin: bark')
        print('bark self:', self)


class DogMetaClass(type):
    def __new__(cls, name, base, attrs):
        # 注意，这里进来了2词，相当于在创建dog类的时候进来一次，创建hashiqi类的时候又进来一次
        print('enter dogmetaclass')  # 在类的定义的时候就进来了
        print('cls', cls)
        print('name', name)
        print('base', base)
        print('attrs', attrs)
        print(super(DogMetaClass, cls))
        new_class = super(DogMetaClass, cls).__new__(cls, name, base, attrs)
        print(new_class) # <class '__main__.Dog'>，返回的是类
        return new_class


# 可以先不看功能类
class Dog(Animal, RunMixin, BarkMixin, metaclass=DogMetaClass):
    def __init__(self):
        print('enter Dog class')
        super().__init__()
        self.address = 'china'


class Hasiqi(Dog):
    def __init__(self, name, age):
        print('enter hashiq class')
        super(Hasiqi, self).__init__()  #注意super返回就是对象。。，fang方法不用带第一个参数self
        self.name = name
        self.age = age

    def bark(self):
        print('Hasiqi bark')
        print('bark self', self)
print('------上面是定义类，下面是创建类的对象 --------')
a = Hasiqi('douzi', 3)