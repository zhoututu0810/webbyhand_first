class ClassDecorator:        #类装饰器的名称
    def __init__(self,function_or_cls):  #这里相当于是第一层，作用是将需要装饰的类名、或者是函数名传递进来
        #这里可以添加额外信息
        self.cls=cls         #或者是self.function=function,本质是要构造 一个属性
        #这里可以添加额外信息
    def __call__(self,name,age):  #这相当于是第二层的wrapper，参数需要与被装饰的类、被装饰的函数，参数相同
        #这里可以增加额外信息
        s=self.cls(name,age)       #本质是调用原来的函数或者类的构造函数
        #result=self.function(a,b)
        #这里可以增加额外信息
        return s                  #返回创建的学生实例s

