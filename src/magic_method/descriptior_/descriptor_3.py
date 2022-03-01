class Constraint_Property(object):
    def __init__(self, var_name, var_type, var_default_value=None):
        '''
        var_name:变量名称
        var_type:变量所要约束的类型，比如int、str、float等等
        var_default_value:变量的初始默认值
        '''
        self.name = var_name
        self.type = var_type
        self.default = var_type() if var_default_value is None else var_default_value   # var_type(), 类似list()
        # 三元运算，如果使用了默认值就使用默认值，否则就是用某个类型的默认值，如int()、str()、float()

    def __get__(self, instance, owner):
        if self.default == None:
            return self.type()
        else:
            return self.default

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("属性的值必须是： %s 类型", self.type)
        self.default = value

    def __delete__(self, instance):
        raise AttributeError("不能删除该属性")


class Student(object):
    name = Constraint_Property("name", str, "张三")  # str虽然是类名，也是可以作为参数的，因为一切皆对象
    age = Constraint_Property("age", int)  # int虽然是类名，也是可以作为参数的，因为一切皆对象


stu = Student()
print(stu.name)
print(stu.age)
stu.name = "李四"
print(stu.name)
stu.age = 25
print(stu.age)
print('===================================')
stu.name = 100.0  # 赋一个实数值

