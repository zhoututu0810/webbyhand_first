"""
lazy - Decorators and utilities for lazy evaluation in Python
Alberto Bertogli (albertito@blitiri.com.ar)
"""


class _LazyWrapper:
    """Lazy wrapper class for the decorator defined below.
    It's closely related so don't use it.
    We don't use a new-style class, otherwise we would have to implement
    stub methods for __getattribute__, __hash__ and lots of others that
    are inherited from object by default. This works too and is simple.
    I'll deal with them when they become mandatory.
    """

    def __init__(self, f, args, kwargs):
        self._override = True
        self._isset = False
        self._value = None
        self._func = f
        self._args = args
        self._kwargs = kwargs
        self._override = False

    def _checkset(self):
        print('111111111111', self._isset, self._value)
        if not self._isset:
            self._override = True
            self._value = self._func(*self._args, **self._kwargs)
            self._isset = True
            self._checkset = lambda: True   # 这是啥意思，自己给自己赋值？
            self._override = False

    def __getattr__(self, name):
        print('----------getattr----', name)
        if self.__dict__['_override']:
            return self.__dict__[name]
        self._checkset()
        print('@@@@@@@@@', self._value, type(self._value), name, self._value.__getattribute__(name))
        return self._value.__getattribute__(name)

    def __setattr__(self, name, val):
        print('----------setattr----', name, val)
        if name == '_override' or self._override:
            self.__dict__[name] = val   # 问题：这个self是谁的对象？
            # 这里只能用这种方法赋值，用点赋值会造成无限循环啊，傻逼，之前不是在描述符知识点看过吗
            return
        self._checkset()
        print('222222222222222')
        setattr(self._value, name, val)     # 这又是什么赋值方式？ 给一个计算结果value设置属性？
        return


def lazy(f):
    """Lazy evaluation decorator"""
    def newf(*args, **kwargs):
        return _LazyWrapper(f, args, kwargs)

    return newf


@lazy
def quick_exe():
    print('---------quick exe-----------')
    return 'quickquick' # 假如这是一个对象


# import pdb
# pdb.set_trace()

quick_exe()
print('#####################')
print(quick_exe())

