import sys
import time
# 为什么，为什么会执行到celery模块去啊，醉了
print(sys.path)
print(__name__)
with open('dubug.log', 'w', encoding='utf-8') as f:
     f.writelines(sys.path)
# 这是在pycharm中执行的结果
# ['/Users/alice/PycharmProjects/webbyhand_first/src/learncelery',    # 当前目录
#  '/Users/alice/PycharmProjects/webbyhand_first',    # 项目目录
#  '/Users/alice/PycharmProjects/webbyhand_first/src',    # 父目录
#  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python37.zip',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7/lib-dynload',
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages',   # 是虚拟目录啊
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg',
#  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']
# # 会将当前目录加入到python的环境路径中
# ['/Users/alice/PycharmProjects/webbyhand_first/src/learncelery2',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python37.zip',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7',
#  '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7/lib-dynload',
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages',
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
#  '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg']

from celery import Celery

redis_url = 'redis://:123456@localhost:6379/0'
backend_rul = 'redis://:123456@localhost:6379/1'
app = Celery('testapp', broker=redis_url, backend=backend_rul)


@app.task
def add(x, y):
    time.sleep(5)
    raise KeyError
    return x + y


if __name__ == '__main__':
    print('我进入了main')
    print('在main中执行就相当于python 执行该模块')
    print('在main模块中的任务，因为不知道具体的模块名，因为当前模块名变成了"__main__",所以找不到注册的任务')
    print('那么此时模块名就用app名称来代替')
    result = add.delay(1, 3)
    print(type(result))
    print(result.ready())
    print(result.get()) # 阻塞方法，会一直等待结果返回！如果任务抛出异常，那么get会同样抛出该异常
    # print(result.get(timeout=10)) # 阻塞方法，就是等待6s
    print(result.traceback)
    print('证明任务调用是异步的')

›

# [2020-07-11 17:47:21,822: ERROR/MainProcess] Received unregistered task of type 'task.add'.
# The message has been ignored and discarded.
#
# Did you remember to import the module containing this task?
# Or maybe you're using relative imports?
