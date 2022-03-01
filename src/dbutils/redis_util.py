import redis
import json
from src.utils.str_util import mydecode, detect_encoding

redis_conf = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 0,
    "password": "123456",
    "decode_responses": True    # redis默认返回字节串，编码类型是utf-8, 该参控控制返回字符串，好用
}
# RedisPy库提供两个类Redis和 StrictRedis 来实现Redis的命令操作。
# StrictRedis实现了绝大部分官方的命令，参数也一一对应，比如set()方法就对应Redis命令的set方法。而Redis是StrictRedis的子类，
# 它的主要功能是用于向后兼容旧版本库里的几个方法。为了做兼容，它将方法做了改写，比如lrem()方法就将value和num参数的位置互换，这和Redis命令行的命令参数不一致。
# 官方推荐使用StrictRedis，所以本节中我们也用StrictRedis类的相关方法作演示。

# rds = redis.StrictRedis(**redis_conf)
# print(rds.get('str_name'))  # 返回的字节串

# 连接池对象，用法就是一个共享对象（什么是共享对象？最为其他实例化的参数）
rds_pool = redis.ConnectionPool(**redis_conf)
print(rds_pool)
rds = redis.StrictRedis(connection_pool=rds_pool)   # 这里必须是命名关键字参数，不能不带名称
print(rds)
print(rds.get('str_name'))

# ### 操作 字符串
# 实例：key value

# ### 操作 hash哈希
# 实例： key dict:{field1:value; field2:value2}
# python ： hset(name, key, value)  这里的name就是指的上面的key,这里的key就是上面的field
print('测试 操作 hash哈希')
# 单个设置field value
rds.hset(name='key_hash_1', key='aa', value=11)
# 批量设置field value
hash_map = {'a': 1, "b": 2, "c": 3}
rds.hmset('key_hash_2', hash_map)

# 取值
print(type(rds.hkeys(name='key_hash_2')), rds.hkeys(name='key_hash_2'))
print(type(rds.hgetall(name='key_hash_2')), rds.hgetall(name='key_hash_2'))
print(rds.hget(name='key_hash_2', key='a'))
print(rds.hmget(name='key_hash_2', keys=['a', 'b']))
# ### 操作 列表list



# ### 操作 集合 set
# print(rds.smembers("_kombu.binding.celery.pidbox"))
# print(rds.smembers("_kombu.binding.celery"))
# print(rds.smembers("_kombu.binding.celeryev"))
print()
for item in rds.smembers("_kombu.binding.celery.pidbox"):
    # print(type(item))
    # testb = item.encode('utf=8')
    # print(type(testb))
    # print(testb)
    # print(detect_encoding(item))
    print("_kombu.binding.celery.pidbox")
    print(item)

for item in rds.smembers("_kombu.binding.celery"):
    print('_kombu.binding.celery')
    print(item)

for item in rds.smembers("_kombu.binding.celeryev"):
    print('_kombu.binding.celeryev')
    print(item)


