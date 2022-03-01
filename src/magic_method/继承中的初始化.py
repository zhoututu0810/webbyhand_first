class Animal:
    name = '类中老虎'

    def __init__(self, name='父类实例的老虎', age=5):
        print("初始化Animal")
        self.name = name
        self.age = age

    def eat(self):
        return '我需要吃东西！'

    @classmethod
    def sleep(cls):
        return '我需要睡觉'


class Dog(Animal):
    color ='red'

    def __init__(self, size):
        print("初始化Dog")
        self.size = size



d = Dog(8)
print(d.__dict__)
print(Dog.__dict__)
print(Animal.__dict__)
print(d.name)
print(d.age)

if __name__ == '__main__':
    pass