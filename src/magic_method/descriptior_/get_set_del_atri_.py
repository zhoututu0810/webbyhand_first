# 简称 magic method 魔法方法
# 作用： 在赋值，取值，删除值得时候可以自定义小动作！
# https://blog.csdn.net/yusuiyu/article/details/87945149

# __getattr__  可以称作兜底方法或者备胎方法
# 当我们访问一个不存在的属性的时候，会抛出异常，提示我们不存在这个属性。而这个异常就是__getattr__方法抛出的，
# 其原因在于他是访问一个不存在的属性的最后落脚点，作为异常抛出的地方提示出错再适合不过了


class A(object):
    def __init__(self, value):
        print('into init method')
        self.value = value

    def __getattr__(self, item):
        print("into __getattr__")
        return "can not find"

    def __setattr__(self, name, value):
        print("into __setattr__")
        if value == 10:
            print
            "from __init__"
        # self.name = value   写成这样会造成死循环，因为复制会调用自身setattr方法，一直反复调用
        object.__setattr__(self, name, value)  # 注意这个固定写法套路
        # self.__dict__[name] = value # 这种方法也可以避免死循环

    def __getattr__(self, item):
        return "when can not find attribute into __getattr__"
        self.__dict__.pop(item)     # 这种写法避免死循环


a = A(10)  # into __init__ # into __setattr__  # from __init__
print(a.value)  # 10
print(a.name)  # into __getattr__  # can not find

# __setattr__, 在对一个属性设置值的时候，会调用到这个函数，每个设置值的方式都会进入这个方法。
a.value = 100   # # into __setattr__
# 需要注意的地方是，在重写__setattr__方法的时候千万不要重复调用造成死循环。object.__setattr__(self, name, value)  # 注意这个固定写法套路

#
del a.value     # when can not find attribute into __getattr__


if __name__ == '__main__':
    pass
