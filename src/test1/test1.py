import os
from collections import Counter
from pathlib import Path
import settings

from importlib import import_module
from importlib.util import find_spec as importlib_find


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        ) from err



# 类装饰器
class cached_property:
    # 问题：为什么要用描述符，描述符的作用，假如这个装饰器不是描述符呢？
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.

    A cached property can be made out of an existing method:
    (e.g. ``url = cached_property(get_absolute_url)``).
    The optional ``name`` argument is obsolete as of Python 3.6 and will be
    deprecated in Django 4.0 (#30127).
    """
    name = None

    @staticmethod
    def func(instance):
        raise TypeError(
            'Cannot use cached_property instance without calling '
            '__set_name__() on it.'
        )

    def __init__(self, func, name=None):
        self.real_func = func   # 保存原始方法
        self.__doc__ = getattr(func, '__doc__')

    def __set_name__(self, owner, name):
        print(name)     # templates 是描述符对象名字
        if self.name is None:
            self.name = name
            self.func = self.real_func
        elif name != self.name:
            raise TypeError(
                "Cannot assign the same cached_property to two different names "
                "(%r and %r)." % (self.name, name)
            )

    # 假设这个不是get,只是一个普通的函数，那么就要用待括号的普通调用方法方式，也可以啊！
    # 用get方法，就变成了属性的调动方式
    def __get__(self, instance, cls=None):
        # get函数首先要明白函数变量缓存在哪里，
        """
        Call the function and put the return value in instance.__dict__ so that
        subsequent attribute access on the instance returns the cached value
        instead of calling cached_property.__get__().
        """
        if instance is None:    # instance是调用方 EngineHandler object
        # 问题：instance是不是空，要看调动，是实例调用，还是方法调用，因为是self调动，所以是实例调用！不为空
            return self
        # 注释这个三个等号！原始函数调用处，将原始函数的结果，保存在属性中
        # 如果不用缓存，下次如果我还要获取节骨，怎么获取？
        # res = self.func(instance)
        res = instance.__dict__[self.name] = self.func(instance)    # 问题：为啥self.func需要传递参数：
        # 首先要明白func是什么 func是EngineHandler.templates, 不是当前类的方法，所以必须要传参
        return res


class EngineHandler:
    def __init__(self, templates=None):
        """
        templates is an optional list of template engine definitions
        (structured like settings.TEMPLATES).
        """
        self._templates = templates
        self._engines = {}

    @cached_property
    # 碰到装饰器，要理清2件事，1首先要理解没有被装饰钱，函数干了啥； 那加了装饰器，改变了啥？
    def templates(self):        # 装饰器 预编译 要清楚这句话等于什么 templates = cached_property(func=templates)
        if self._templates is None:
            self._templates = settings.TEMPLATES

        templates = {}
        backend_names = []
        for tpl in self._templates:
            try:
                # This will raise an exception if 'BACKEND' doesn't exist or
                # isn't a string containing at least one dot.
                default_name = tpl['BACKEND'].rsplit('.', 2)[-2]
            except Exception:
                invalid_backend = tpl.get('BACKEND', '<not defined>')
                raise Exception(
                    "Invalid BACKEND for a template engine: {}. Check "
                    "your TEMPLATES setting.".format(invalid_backend))

            tpl = {
                'NAME': default_name,
                'DIRS': [],
                'APP_DIRS': False,
                'OPTIONS': {},
                **tpl,      # 字典还能真么用，卧槽了，待测试一下
            }

            templates[tpl['NAME']] = tpl
            backend_names.append(tpl['NAME'])

        counts = Counter(backend_names)
        duplicates = [alias for alias, count in counts.most_common() if count > 1]
        if duplicates:
            raise Exception(
                "Template engine aliases aren't unique, duplicates: {}. "
                "Set a unique NAME for each engine in settings.TEMPLATES."
                .format(", ".join(duplicates)))

        return templates

    def __getitem__(self, alias):
        try:
            return self._engines[alias] # 这是是什么时候进入的？
        except KeyError:
            try:
                params = self.templates[alias]
            except KeyError:
                pass

            # If importing or initializing the backend raises an exception,
            # self._engines[alias] isn't set and this code may get executed
            # again, so we must preserve the original params. See #24265.
            params = params.copy()
            backend = params.pop('BACKEND')
            engine_cls = import_string(backend)
            engine = engine_cls(params) # 参考单例，这一句才是缓存的核心？一个对象被创建后，就不会释放了。什么样的对象可以用单例。工具类或工厂类！

            self._engines[alias] = engine
            return engine

    def __iter__(self):
        print(self.templates)
        return iter(self.templates) # 如果描述符合属性同名，先访问哪个？

    def all(self):
        return [self[alias] for alias in self]


engines = EngineHandler()

def _engine_list(using=None):
    return engines.all() if using is None else [engines[using]]

if __name__ == '__main__':
    engines = _engine_list(using=None)

