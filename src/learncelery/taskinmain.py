import sys
# 为什么，为什么会执行到celery模块去啊，醉了
print(sys.path)
['/Users/alice/PycharmProjects/webbyhand_first/src/learncelery',    # 当前目录
 '/Users/alice/PycharmProjects/webbyhand_first',    # 项目目录
 '/Users/alice/PycharmProjects/webbyhand_first/src',    # 父目录
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
 '/Users/alice/.pyenv/versions/3.7.7/lib/python37.zip',
 '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7',
 '/Users/alice/.pyenv/versions/3.7.7/lib/python3.7/lib-dynload',
 '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages',   # 是虚拟目录啊
 '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
 '/Users/alice/PycharmProjects/webbyhand_first/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg',
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']


from celery import Celery

redis_url = 'redis://:123456@localhost:6379/0'
app = Celery('task', broker=redis_url)


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    add.delay()