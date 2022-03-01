# 学习并封装kafka-python
# 参考: https://www.jianshu.com/p/877e59f59321

import sys
import time
import json

from kafka import KafkaProducer
from kafka import KafkaConsumer, TopicPartition
from kafka.errors import KafkaError

BOOTSTRAP_SERVERS = 'localhost:9092'
mytopic = 'test'
"""
# class kafka.KafkaProducer(**configs)
# json用于发送json字符串，如果是发送一般的字符串，不能用该参数哦！！
# producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
#                          value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
# send(topic, value=None, key=None, headers=None, partition=None, timestamp_ms=None)
future = producer.send(topic=ONE_TOPIC, value=b'first message')
# get是一个阻塞方法哦，显而易见啦，有timeout参数
result = future.get(timeout=60)
print(result)
# RecordMetadata(topic='test', partition=1, topic_partition=TopicPartition(topic='test', partition=1), offset=1,
#                timestamp=1590227119569, checksum=None, serialized_key_size=-1, serialized_value_size=13, serialized_header_size=-1)
"""

# class kafka.KafkaConsumer(*topics, **configs),实例化方法不会触发请求kafka服务
consumer = KafkaConsumer(mytopic, bootstrap_servers=BOOTSTRAP_SERVERS, auto_offset_reset='earliest')
# 这个方法很重要，因为它会触发去请求服务器哦！
topics_set = consumer.topics()  # 返回所有topics
# print('topics_set', topics_set)     # {'test'}
# Get the current topic subscription.   # 订阅的对象是topic
# subscription = consumer.subscription()
# print('subscription\n', subscription)   # {'test'}

# 上面的方法不重要，下面的才是重要的方法
# 这个方法也会请求服务器, 查询某个topic下的所有分片
partition_ids_set = consumer.partitions_for_topic(mytopic)
# print('partition_ids_set ：', partition_ids_set)     # {0, 1}

# ### 最重要的对象之一，TopicPartition对象，表示一个topic的某个分片
# 查看分配给该topic的分片，返回的是一个TopicPartition对象的集合{},集合可以直接迭代遍历
tps = consumer.assignment()     # 注意这个方法不会触发查询服务端
# print(type(tps))    # <class 'set'>
#  {TopicPartition(topic='test', partition=1), TopicPartition(topic='test', partition=0)}
# print('topic_partition_set :', tps)

# 也可以自己构造topicPartition对象,注意tps是TopicPartition对象的里诶啊哦
# tps = [TopicPartition(mytopic, p) for p in consumer.partitions_for_topic(mytopic)]
# 然后分配给topic
# 为consumer分配分区
# consumer.assign(tps)

# 返回的是"每个分片"的起始位置和最后位置，所以是个set
begin_offset = consumer.beginning_offsets(tps)  # 注意: 这个方法不会触发查询服务端
# b{TopicPartition(topic='test', partition=0): 2, TopicPartition(topic='test', partition=1): 2}
# print('begin_offset: ', begin_offset)
end_offset = consumer.end_offsets(tps)
# {TopicPartition(topic='test', partition=0): 2, TopicPartition(topic='test', partition=1): 2}
# print('end_offset: ', end_offset)

# seek重新定位函数
# 定位到开始
# consumer.seek_to_beginning(*tuple(tps)) # 定位到begging_offset地方，开始的地方
# 定位到结束
# consumer.seek_to_end(*tuple(tps))   # 定位到end_offset的位置，待进入的消息位置处
# 定位到指定地点, 问题？set集合不能直接用索引取数吗，肯定不行啊，傻逼，set没有顺序
consumer.seek(list(tps)[0], 0)
consumer.seek(list(tps)[1], 0)
# print("重新制定后再查看当前消费位置：", consumer.position(list(tps)[0]))   # 重新制定后再查看当前消费位置： 0

# 查看当前消费者每个分区消费到的位置
# 这种迭代方法也可以
for tp in tps:
    p2 = consumer.position(tp)
    print('当前分片消费位置p2: ', p2)   # 2，2 (两个分片只有两个数据，位置是0，1，结果返回2，说明最后一条数据+1)
    # position是即将uncoming消息的位置，是最后一条消息的位置+1，注意不是最后1条消息处

# kafka.errors.IllegalStateError: IllegalStateError: You must choose only one way to configure your consumer:
# 以下三种方法冲突
# (1) subscribe to specific topics by name,  通过制定topic名称订阅，也就是生产和消费的类实例化的时候
# (2) subscribe to topics matching a regex pattern,
# (3) assign itself specific topic-partitions.  通过assign方法，指定topic-partion对象来分配，
# consumer.assign(list(tps))

# 查看当前实例分配的tp
print(consumer.assignment())

# 这是一个循环等待函数, 一直在监控数据，有数据进来就会执行，太吊了！！
# 为什么消费不到历史消息？
for msg in consumer:        # 这是一个无限循环哦，一直等到拿到数据
    print(1)
    print('msg1:', msg)
    print(msg.value)        # 最重要的方法哈，
# msg1: ConsumerRecord(topic='test', partition=0, offset=0, timestamp=1590216532232, timestamp_type=0, key=None,
# value=b'1', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=1, serialized_header_size=-1)

# 待查看是不是数据被丢失了！！！