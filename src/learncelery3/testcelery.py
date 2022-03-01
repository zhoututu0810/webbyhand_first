#
from celery import Celery
from celery import task
from celery import shared_task
from celery.local import Proxy
from celery.result import AsyncResult
from celery import signature
from celery import maybe_signature


redis_url = 'redis://:123456@localhost:6379/0'
backend_rul = 'redis://:123456@localhost:6379/1'
app = Celery('taskinmain', broker=redis_url, backend=backend_rul)

def add1(x, y):
    return x + y

print(add1)     # <function add1 at 0x1085385f0>
print(add1.__name__)    # add1

@app.task    # 注册任务，任务的名称肯定就是app的名字 taskinmain+函数名，这个好理解吧！！！
def add2(x, y):
    return x + y

@share_task
def add3(x, y):
    return x + y

print(add2)         # <@task: taskinmain.add2 of taskinmain at 0x10b231050>
print(add2.name)    # taskinmain.add2
print(app.tasks)
# {'taskinmain.add2': <@task: taskinmain.add2 of taskinmain at 0x10f831050>,
# 'celery.chunks': <@task: celery.chunks of taskinmain at 0x10f831050>,
# 'celery.chord_unlock': <@task: celery.chord_unlock of taskinmain at 0x10f831050>,
# 'celery.group': <@task: celery.group of taskinmain at 0x10f831050>, 'celery.backend_cleanup':
# <@task: celery.backend_cleanup of taskinmain at 0x10f831050>,
# 'celery.map': <@task: celery.map of taskinmain at 0x10f831050>,
# 'celery.chain': <@task: celery.chain of taskinmain at 0x10f831050>,
# 'celery.starmap': <@task: celery.starmap of taskinmain at 0x10f831050>,
# 'celery.chord': <@task: celery.chord of taskinmain at 0x10f831050>,
# 'celery.accumulate': <@task: celery.accumulate of taskinmain at 0x10f831050>}


if __name__ == '__main__':
    # add2.delay()        # 问题在于我发送消息
    pass