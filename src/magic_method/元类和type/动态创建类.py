# type通常用法就是用来判断对象的类型（就是判断对象是参照什么模板生成的）。但除此之外，他最大的用途是用来动态创建类。
# 当Python扫描到class的语法的时候，就会调用type函数进行类的创建。
# 首先，type()需要接收三个参数
# 1. 类的名称，若不指定，也要传入空字符串：""
# 2. 父类，注意以tuple的形式传入，若没有父类也要传入空tuple：()，默认继承object
# 3. 绑定的方法或属性，注意以dict的形式传入
# 类 = type()


class BaseClass(object):
    def talk(self):
        print("talk")


# 注意这个方法在类的外面，但是第一个参数还是self
def func1(self):
    return "func1"


# 动态创建类11 d1 = collections.OrderedDict()
# 字典中的key-value，既可以表示属性，也可以表示方法，看值value是什么
# User本身就是一个变量，默认和类名一致
User = type('User', (BaseClass,), {"name": "user", "func1": func1})
u1 = User()
print(u1.name)
print(u1.func1())

# 上面是动态创建类，class是type()方法的语法糖
# 上面是动态创建类，class是type()方法的语法糖
# 上面是动态创建类，class是type()方法的语法糖


# ###########################################################################
# type用来自定义元类
# 元类的特性就是__new__()方法
# 类似类的特性是__init__()方法

# 类的作用是创建对象，使得对象中有相同的动态属性和方法
# 元类的作用是创建类，使得类中有相同的预先定义好的 类属性和类方法
# ###########################################################################
def func2(cls):
    return "我是一个类方法"

class BaseClass2(type):

    def __new__(cls, *args, **kwargs):
        print("元类的new方法，创建类对象")
        # 调用父元类type中的构造方法
        # 参数是当前类，给类绑定一些类方法和类属性，init的参数是当前对象
        return super().__new__(cls, *args, **kwargs)


class User2(metaclass=BaseClass2):
    def __init__(self):
        print("User2 init")

u1 = User2()
print()
# 结论：实例化方法(创建对象)之前，会首先创建类。在init方法前，会执行new方法

@classmethod   # 注意加这个装饰器才能绑定类方法
def func3(cls):
    print(1)

# type可以直接生成类（class），但也可以先生成元类（metaclass），再使用元类批量定制类（class）。
# 元类均被命名后缀为Metalass，元类的生命周期：
class SayMetaClass(type):
    # 元类是由“type”衍生而出，所以父类需要传入type。
    # cls永远指向书写所在的类
    def __new__(cls, name, bases, attrs):
        print(cls.__name__)     # SayMetaClass， 当前书写所在的类
        print(name)             # Hello，即将待创建的类名
        print(bases)            # 待创建类的父类，是一个tuple
        print(attrs)            # 待创建的类中的属性，类中可以定义类属性，实例属性，类变量，实例变量
        # 元类的操作都在 __new__中完成，它的第一个参数是当前所在类，之后的参数即是三大永恒命题：类名，基类，类的成员（一般就是操作类的成员了，类的成员就是类的__dict__）。
	    # 最常用的操作就是操作attrs属性了
        # 创造属性和方法，由元类创建的类叫“Hello”，那创建时就自动有了一个叫“say_Hello”的类方法
        # 然后又将类的名字“Hello”作为默认参数saying，传到了方法里面。
        # 然后把hello方法调用时的传参作为value传进去，最终打印出来。
        # saying=mame是默认参数
        # 这个是绑定实例属性
        attrs['say_' + name] =lambda self, value, saying=name: print(saying + ',' + value + '!')

        # 也可以绑定类属性, 添加失败，不是这么添加类属性？
        attrs['clsfunc'] = func3

        # 传承类名，父类，属性
        return type.__new__(cls, name, bases, attrs)


class Hello(object, metaclass =SayMetaClass):
    # 创建类，通过元类创建的类，第一个参数是父类，第二个参数是metaclass
    pass

hello =Hello()# 创建实列
hello.say_Hello('bobo')# 调用实例方法
hello.clsfunc()
Hello.clsfunc()
print()
# class Nihao(object,metaclass=SayMetaClass):
#     pass
#
# nihao=Nihao()
# nihao.say_Nihao("greg 李")