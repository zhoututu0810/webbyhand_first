# 证明生成器执行完就close了
from inspect import getgeneratorstate
def gen():
    print('init gen')
    arg = yield 1
    print('done')
g=gen()
print(getgeneratorstate(g))     # GEN_CREATED
print(g.send(None)) # 等同于next(g)
print(getgeneratorstate(g))     # GEN_SUSPENDED
try:
    g.send(1)
except StopIteration as e:
    print('捕获stop异常')
    print(getgeneratorstate(g)) # GEN_CLOSED


# 异步IO基本式
from ladder import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")
    # 当执行完毕后，生成器状态变为close的。

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())  # 类似线程的join等待同步操作！！！
# compete可以看做是检查生成器的状态，是否是close的。
# 事件循环的作用可以通过端口或者其他啥的，监控IO操作的状态，一旦监测到异步IO完成了，就会在队列中防止一个 任务.send()，排队去一个一个
# 的触发携程任务函数继续执行
print('main close ')
loop.close()

# 问题是为什么要用yeilf from代理
# 是为了代理系统自定义的携程对象！！！
