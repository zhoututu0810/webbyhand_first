class MethodDecorator:
    def __init__(self, function):
        print('enter init')
        self.function = function

    def __call__(self):
        print('开始 call')
        self.function()
        print('结束 call')


@MethodDecorator
def myfunc():
    print('我是函数myfunc')

print(myfunc) # 此时函数已经替换成了实例 <__main__.MethodDecorator object at 0x10ebe0150>

# 执行函数
myfunc()

