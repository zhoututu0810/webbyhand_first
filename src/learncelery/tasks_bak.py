from celery import Celery
# from . import celeryconfig  报错 ImportError: attempted relative import with no known parent package
import celeryconfig  # 必须这么写，我去

# 设置redis作为消息队列broker
# Celery第一个参数就是应用名称，一个Celery实例就是一个应用
# app = Celery('demo', broker='redis://:123456@localhost:6379/0')
# app = Celery('demo', broker='redis://:123456@localhost:6379/0', backend='redis://:123456@localhost:6379/1')
app = Celery('demo')
app.config_from_object('celeryconfig')

# 创建任务函数,注意这里的app就上上面的celery对象app，很牛逼吧
@app.task
def my_task():
    print("任务函数正在执行")



