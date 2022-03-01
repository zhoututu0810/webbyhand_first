# 命名元祖
# 注意：命名元祖中的值是key-value形式，类似字典，不是类似元祖，不知道为啥叫命名元祖
# 这个命名元祖namedtuple里面相反的，orderddict里面保存的元祖，namedtuple里面保存的是字典，坑啊

# 看一下源码定义
################################################################################
### namedtuple
################################################################################
# 参数typename：类型名
# 参数field_names：字段名
# 参数defaults： 字段的默认值！

# def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
#     """Returns a new subclass of tuple with named fields.
#
#     >>> Point = namedtuple('Point', ['x', 'y'])
#     >>> Point.__doc__                   # docstring for the new class
#     'Point(x, y)'
#     >>> p = Point(11, y=22)             # instantiate with positional args or keywords
#     >>> p[0] + p[1]                     # indexable like a plain tuple  # 居然可以索引！毕竟叫做元祖嘛
#     33
#     >>> x, y = p                        # unpack like a regular tuple  # 相当于按位置取值！
#     >>> x, y
#     (11, 22)
#     >>> p.x + p.y                       # fields also accessible by name
#     33
#     >>> d = p._asdict()                 # convert to a dictionary # 去掉命名元祖的名字，剩下的值就是一个字典
#     >>> d['x']
#     11
#     >>> Point(**d)                      # convert from a dictionary   # 这个就是本质精髓，就是字典初始化过来的
#     Point(x=11, y=22)
#     >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
#     Point(x=100, y=22)
#
#     """
#
#     # Validate the field names.  At the user's option, either generate an error
#     # message or automatically replace the field name with a valid name.
#     if isinstance(field_names, str):
#         field_names = field_names.replace(',', ' ').split()
#     field_names = list(map(str, field_names))
#     typename = _sys.intern(str(typename))

from collections import namedtuple

# namedtuple是一个类工厂，不是对象工厂，得到对象要2步
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry.name)


# 第二个初始化方法，和上面是一样，只是字段参数可以是字符串，也可以是列表
Cursor = namedtuple('Cursor', ['offset', 'reverse', 'position'])
PageLink = namedtuple('PageLink', ['url', 'number', 'is_active', 'is_break'])

PAGE_BREAK = PageLink(url=None, number=None, is_active=False, is_break=True)