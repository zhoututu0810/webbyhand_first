# celery配置文件
from kombu import Exchange, Queue
broker_url = 'redis://:123456@localhost:6379/0'         # redis第一个数据库
result_backend = 'redis://:123456@localhost:6379/1'     # redis第二个数据库



