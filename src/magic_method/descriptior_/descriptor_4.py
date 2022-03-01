class IntField:
    def __init__(self, value):
        print('enter init')
        self.value = value

    def __get__(self, instance, owner):
        print('11111')
        if instance is None:
            return self
        return instance.__dict__[self.name]  # 另一种方法保存属性！！！不是保存在描述符对象中

    def __set__(self, instance, value):
        print(2222)
        if not isinstance(value, int):
            raise ValueError('expecting integer')
        instance.__dict__[self.name] = value        # 给对象添加一个a=1,

    def __set_name__(self, owner, name):        # 测试发现该方法在实例化的时候回自动执行，自动获取属性描述符对象的名字
        print('enter set_name')
        print(owner)
        print(name)     # a
        print(type(name))   # <class 'str'>
        self.name = name    # 给当前IntField对象添加一个name属性，属性值是 描述符对象的字符串名字


class Example:
    a = IntField('initarg')

print('开始测试')
e = Example()
e.a = 2
print()
print(e.a)
# Example.a = 1       # 为什么进入是3，而不是二
