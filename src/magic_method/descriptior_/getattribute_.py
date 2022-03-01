class Animal(object):
    run = '我会跑'

    def die(self):
        return '我会死'


class Dog(Animal):
    color = 'Blue'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写__getattribute__。需要注意的是重写的方法中不能
    # 使用对象的点运算符访问属性，否则使用点运算符访问属性时，
    # 会再次调用__getattribute__。这样就会陷入无限递归。
    # 可以使用super()方法避免这个问题。
    def __getattribute__(self, key):
        print('调用了__getattribute__属性')
        return super(Dog, self).__getattribute__(key)

    def sound(self):
        return "汪汪汪"


dog = Dog('泰迪', 4)  # 实例化赋值的时候不会调用
print(dog.name, end='\n------------------------------\n')  # 调用实例属性
# print(dog.age, end='\n------------------------------\n')
# print(dog.color, end='\n------------------------------\n')  # 调用方法属性
# print(dog.run, end='\n------------------------------\n')  # 调用父类的类属性
# print(dog.sound(), end='\n------------------------------\n')  # 调用实例方法
# print(dog.die(), end='\n------------------------------\n')  # 调用父类的方法

