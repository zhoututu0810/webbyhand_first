# 介绍 __str__(self) 和 __rper__(self)的区别
class Car():
    def __init__(self, name):
        self.name = name

    # print会触发调用str方法
    # def __str__(self):        # str方法默认实现是调用rper方法，所以一般只需要重写rper方法就行
    #     print('enter str method')


    def __repr__(self):
        print('enter rper method')
        return 'rper'

print(Car('A'))
