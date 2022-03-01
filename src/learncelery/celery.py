from celery import Celery
# import celeryconfig

# 创建一个celer应用
app = Celery('demo')
app.config_from_object('learncelery.celeryconfig')

# 自动搜索任务
app.autodiscover_tasks(['learncelery'])


