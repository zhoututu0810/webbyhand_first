class NewDefine_classmethod:
    """
    使用“描述符”和“装饰器”结合起来，模拟@classmethod
    """

    def __init__(self, function):
        self.function = function

    def __get__(self, instance, owner):
        # 对传进函数进行加工,最后返回该函数
        print('instance', instance)     # instance None, 因为此时是类调动，不是对象调用
        print('owner', owner)           # owner <class '__main__.Person'>

        def wrapper(*args, **kwargs):  # 使用不定参数是为了匹配需要修饰的函数参数
            print("给函数添加额外功能")
            self.function(owner, *args, **kwargs)

        return wrapper


class Person:
    name = '我有姓名'

    def __init__(self):
        pass

    @NewDefine_classmethod
    def study_1(cls):
        print(f'我的名字是：{cls.name},我会搞学习！')

    @NewDefine_classmethod
    def study_2(cls, score):
        print(f'我的名字是：{cls.name},我会搞学习！,而且这次考试考了 {score} 分')


print(Person.study_1())
# print(Person.study_2(99))

