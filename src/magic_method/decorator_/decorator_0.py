# 本篇文章纠正一个误区，装饰器是在什么时候执行替换的
# 装饰器在书写的时候就调用。 类装饰器也会在书写的时候执行init方法，返回一个装饰器类的对象

# 如果装饰器需要接受参数，需要在基本格式在再封装一层， 这个本质是闭包closure
def log(text):
    print('enter log')
    def decorator(func):
        print('enter decarator')    # 预编译可以做的事情  ， 装饰器的装饰功能分2块，以前一直认为只有一块，我操了！！
        def wrapper(*args, **kw):       # 运行过程可以做的海清
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        print('exit decrator')
        return wrapper
    print('exit log')           # 预编译可以做的事情
    return decorator


@log(text='closure arg')
def func():
    print('func 执行')

print('还没开始能')
print()

# 注意，在func函数没有调用的时候，装饰器就已经执行过了，类似预编译了
print(func.__name__)    # 此时函数在编辑的时候就已经被替换了wrapper， 而不是在函数执行的时候


# 问题：那么类装饰器呢
print('测试类装饰器在干嘛')
class DecoratorClass(object):
    def __init__(self, function):
        print('enter init')
        self.function = function

    def __call__(self, *args, **kwargs):
        print('功能1')
        return self.function(*args, **kwargs)

@DecoratorClass
def func(a, b):
    return a + b

