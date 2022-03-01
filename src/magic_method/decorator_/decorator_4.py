class ClassDecorator:
    def __init__(self, cls):  # 这里相当于是第一层，作用是将类名Student传递进来
        print('enter decrator init')    # 这个是第一步
        self.cls = cls
        self.height = 170
        self.weight = 65

    def __call__(self, name, age):  # 这相当于是第二层的wrapper
        print('enter decorator call')
        s = self.cls(name, age)
        s.height = self.height  # 动态添加属性，增加额外信息
        s.weight = self.weight
        return s  # 返回创建的学生实例s


@ClassDecorator
class Student:
    def __init__(self, name, age):
        print('enter 被装饰的类的 init')      # 这个是最后一步
        self.name = name
        self.age = age

print(Student) # 此时类Student已经替换成了实例<__main__.ClassDecorator object at 0x108a8ed50>
stu = Student('张三', 25)  # 注意：这里的Student其实并不是一个类了，而是装饰器返回的一个对象，即这里的Student是ClassDecorator的实例
# 而且，这里的Student('张三',25) 也不是构造函数了，它的本质是装饰类的“对象调用”
# enter decrator init
# enter decorator call
# enter 被装饰的类的 init
# print(stu.name)
# print(stu.age)
# print(stu.height)
# print(stu.weight)

