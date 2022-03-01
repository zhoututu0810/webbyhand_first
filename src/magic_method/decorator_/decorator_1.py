# 为什么看不懂装饰器了！
# 装饰器的基本格式，最低有2层，第一层是接受函数名的 接口函数，里面定义了返回函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
# 调用now(),本质是调用wrapper()

# 如果装饰器需要接受参数，需要在基本格式在再封装一层， 这个本质是闭包closure
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 为什么一碰到装饰器就看不懂了
# 看不懂调用装饰器函数的过程！！
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # 多了这一步，激活生成器
        return gen

    return primer


@coroutine
def averager():
    total = .0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count