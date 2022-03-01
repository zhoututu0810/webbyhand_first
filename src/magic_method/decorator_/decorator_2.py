def Singleton(cls): # 这是第一层函数，相当于模板中的Decorator.目的是要实现一个“装饰器”，而且是对类型的装饰器
    '''
    cls:表示一个类名，即所要设计的单例类名称，
        因为python一切皆对象，故而类名同样可以作为参数传递
    '''
    print('enter Singlton function')
    a = 1
    instance = {}

    def singleton(*args, ** kargs):  # 这是第二层，相当于wrapper，要匹配参数
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return  instance[cls]

    return singleton      # 注意此时返回的是一个函数


@Singleton
class Student(object):
    # def __new__(cls, *args, **kwargs):      # 用了装饰器，又用了new，报错了
    #     print('enter new')
    #     return super(Student, cls).__new__(cls) # TypeError: super() argument 1 must be type, not function

    def __init__(self, name, age):
        print('enter init')
        self.name = name
        self.age = age
        print('exit init')

print(Student)   # <function Singleton.<locals>.singleton at 0x10b0f20e0> 此时Student已经被替换成了函数
# s1 = Student('张三', 23)
# # enter Singlton function
# # enter init
# # exit init
# s2 = Student('李四', 24)
# print((s1 == s2))
# print(s1 is s2)
# print(id(s1), id(s2), sep='   ')

