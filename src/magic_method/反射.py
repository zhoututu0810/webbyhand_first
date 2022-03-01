# 总结：对于对象，
# 对于类，实例属性是返回不了的。英文在实例化的时候才能赋值，所以肯定是没有值的

class Animal(object):
    name = '动物'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func1(self):
        pass

    @classmethod
    def clsfunc1(cls):
        pass


class Dog(Animal):
    def __init__(self, c):
        self.c = c
        super().__init__('a', 'b')  # 这句话的意思是什么？
        # 在子类中执行父类的初始化方法，但是要注意，执行init的self还是子类，
        # 相当于把子类方法函数体的内容放到子类来执行
        # 具体此时没有实例化父类，实例化的还是子类
        # 调用父类的初始化方法，只是把父类的初始化函数中的内容放到子类来执行！！！！
        # 这也解开了一个心结！ 子类调用父类实例化，会实例化分类嘛？ 不会
        # 因为实例化方法也会继承，只是隐形继承，因为和当前类的init方法有冲突，所以搞了一个super()前缀
        # 实际上父类的初始化也继承到子类了，也是子类的方法！！！！java这点说的就很清楚


a = Animal(1, 2)
# 结论：能访问就返回Ture, 反过来，hazattr返回ture，就能够访问
print(hasattr(a, 'a'))           # Ture
print(hasattr(a, 'func1'))       # Ture
print(hasattr(a, 'clsfunc1'))    # Ture
print(hasattr(a, 'name'))       # Ture
# 给类动态添加属性
Animal.b = 'b'
print(hasattr(a, 'b'))      # 可以动态给类添加类属性，因为类也是一个对象，很简单好说吧!


print()
print(hasattr(Animal, 'a'))         # false     # 类不能访问实例属性，所以肯定是false啊！
print(hasattr(Animal, 'func1'))     # ture      # 关键点：类能够访问实例访问！但是却不能调用
print(hasattr(Animal, 'clsfunc1'))  # ture
print(hasattr(Animal, 'name'))      # ture

print()
print('测试子类实例')
d = Dog('c')
print(hasattr(d, 'c'))      # Ture
print(hasattr(d, 'a'))      # Flase : 说明：子类虽然继承父类，但是子类对象跟父类对象却没有关系，对象的关键就是属性，两者没有任何的关系
print(hasattr(d, 'b'))
print(hasattr(d, 'name'))
print(hasattr(d, 'func1'))
print(hasattr(d, 'clsfunc1'))

# 这个说明，子类访问对象的顺序
    # 子类实例
    # 子类    # 子类找不到，再找父类，这是子类的功能
    # 父类    # 注意：全程跟父类实例没有关系！
print()
print('测试子类')
print(hasattr(Dog, 'name'))     # Ture
print(hasattr(Dog, 'func1'))    # Ture
print(hasattr(Dog, 'clsfunc1')) # Ture

