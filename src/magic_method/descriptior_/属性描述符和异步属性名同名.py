# 人的性格描述，悲观的？开朗的？敏感的？多疑的？活泼的？等等
class CharacterDescriptor:
    def __init__(self, value):
        self.value = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print("访问性格属性")
        return self.value


    def __set__(self, instance, value):
        print("设置性格属性值")
        self.__dict__[self.name] = value        # 不用描述符代理，用dict作缓存
        # 我把对象保存在dict中，那为什么要用描述符，可以对set作变更啊。所以描述符分2类，数据描述符和非数据描述符
        # 数据描述符， 如果有set， 重点就在set,而不是get了，所以完全可以用__dict__作为缓存


class Person:
    a2 = CharacterDescriptor('乐观的')

    def __init__(self):
        self.a2 = '悲观的'     # 一旦一个变量被声明为描述符，那就是一个描述符，所以这个设置会调转到描述符代理类的set中去

    # def __getattribute__(self, key):
    #     print('__getattribute__')
    #     return super(Person, self).__getattribute__(key)

    # def __getattr__(self, key):
    #     print('__getattr__')


p = Person()
p.__dict__['a2'] = 'wocao'  # 尽管设置了对象属性，但是访问的永远是属性描述符对象！！！！切记啊，有点反人类。
print(p.a2)

