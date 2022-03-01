# 人的性格描述，悲观的？开朗的？敏感的？多疑的？活泼的？等等
class CharacterDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("访问性格属性")
        print('instance', instance)     # instance    <__main__.Person object at 0x109463950>  对象
        print('owner', owner)           # owner       <class '__main__.Person'>    类
        return self.value

    def __set__(self, instance, value):
        print("设置性格属性值")           # intance是调用者
        print('instance', instance)     # instance    <__main__.Person object at 0x10bb22950>   对象
        print('value', value)           # value 悲伤的
        self.value = value

    def __delete__(self, instance):
        print('delte')
        print(instance)     # <__main__.Person object at 0x1021b1910>
        del self.value


# 人的体重描述，超重？过重？肥胖？微胖？合适？偏轻？太瘦？等等
class WeightDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("访问体重属性")
        return self.value

    def __set__(self, instance, value):
        print("设置体重属性值")
        self.value = value      # value是委托给描述符对象保管的，此时描述符对象就像一个代理



class Person:
    character = CharacterDescriptor('乐观的')
    weight = WeightDescriptor(150)


p = Person()
print(p.character)
p.character = '悲伤的'
del p.character
print(p.character)

