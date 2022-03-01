# 参考 https://blog.csdn.net/learn_tech/article/details/81115996?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

# coding=utf-8

import time
from pykafka import KafkaClient


# pykafka生产者api
class ProductorKafkaTest(object):
    """
    测试kafka常用api
    """

    def __init__(self, host="192.168.237.129:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)

    def producer_partition(self, topic):
        """
        生产者分区查看，主要查看生产消息时offset的变化
        :return:
        """
        topic = self.client.topics[topic.encode()]
        partitions = topic.partitions
        print(u"查看所有分区 {}".format(partitions))

        earliest_offset = topic.earliest_available_offsets()
        print(u"获取最早可用的offset {}".format(earliest_offset))

        # 生产消息之前看看offset
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))

        # 同步生产消息
        p = topic.get_producer(sync=True)
        p.produce(str(time.time()).encode())

        # 查看offset的变化
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))

    def producer_designated_partition(self, topic):
        """
        往指定分区写消息，如果要控制打印到某个分区，
        需要在获取生产者的时候指定选区函数，
        并且在生产消息的时候额外指定一个key
        :return:
        """

        def assign_patition(pid, key):
            """
            指定特定分区, 这里测试写入第一个分区(id=0)
            :param pid: 为分区列表
            :param key:
            :return:
            """
            print("为消息分配partition {} {}".format(pid, key))
            return pid[0]

        topic = self.client.topics[topic.encode()]
        p = topic.get_producer(sync=True, partitioner=assign_patition)
        p.produce(str(time.time()).encode(), partition_key=b"partition_key_0")

    def async_produce_message(self, topic):
        """
        异步生产消息，消息会被推到一个队列里面，
        另外一个线程会在队列中消息大小满足一个阈值（min_queued_messages）
        或到达一段时间（linger_ms）后统一发送,默认5s
        :return:
        """
        topic = self.client.topics[topic.encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))

        # 记录最初的偏移量
        old_offset = last_offset[0].offset[0]
        p = topic.get_producer(sync=False, partitioner=lambda pid, key: pid[0])
        p.produce(str(time.time()).encode())
        s_time = time.time()
        while True:
            last_offset = topic.latest_available_offsets()
            print("最近可用offset {}".format(last_offset))
            if last_offset[0].offset[0] != old_offset:
                e_time = time.time()
                print('cost time {}'.format(e_time - s_time))
                break
            time.sleep(1)

    def get_produce_message_report(self, topic):
        """
        查看异步发送消报告,默认会等待5s后才能获得报告
        """
        topic = self.client.topics[topic.encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))
        p = topic.get_producer(sync=False, delivery_reports=True, partitioner=lambda pid, key: pid[0])
        p.produce(str(time.time()).encode())
        s_time = time.time()
        delivery_report = p.get_delivery_report()
        e_time = time.time()
        print('等待{}s, 递交报告{}'.format(e_time - s_time, delivery_report))
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))


#  pykafka消费者api
class ConsumerKafkaTest(object):
    def __init__(self, host="192.168.237.129:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)

    def simple_consumer(self, topic, offset=0):
        """
        消费者指定消费
        :param offset:
        :return:
        """

        topic = self.client.topics[topic.encode()]
        partitions = topic.partitions
        last_offset = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offset))  # 查看所有分区
        consumer = topic.get_simple_consumer(b"simple_consumer_group", partitions=[partitions[0]])  # 选择一个分区进行消费
        offset_list = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset_list))  # 消费者拥有的分区offset的情况
        consumer.reset_offsets([(partitions[0], offset)])  # 设置offset
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        offset = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset))  # 3

    def balance_consumer(self, topic, offset=0):
        """
        使用balance consumer去消费kafka
        :return:
        """
        topic = self.client.topics["kafka_test".encode()]
        # managed=True 设置后，使用新式reblance分区方法，不需要使用zk，而False是通过zk来实现reblance的需要使用zk
        consumer = topic.get_balanced_consumer(b"consumer_group_balanced2", managed=True)
        partitions = topic.partitions
        print("分区 {}".format(partitions))
        earliest_offsets = topic.earliest_available_offsets()
        print("最早可用offset {}".format(earliest_offsets))
        last_offsets = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offsets))
        offset = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset))
        while True:
            msg = consumer.consume()
            offset = consumer.held_offsets
            print("{}, 当前消费者分区offset情况{}".format(msg.value.decode(), offset))


if __name__ == '__main__':
    host = '192.168.17.64:9092,192.168.17.65:9092,192.168.17.68:9092'

    # 测试消费者
    kafka_ins = ConsumerKafkaTest(host)
    topic = 'test'
    # kafka_ins.simple_consumer(topic)
    kafka_ins.balance_consumer(topic)

    # 测试生产者
    kafka_ins = ProductorKafkaTest(host)
    topic = 'test'
    # kafka_ins.producer_partition(topic)
    # kafka_ins.producer_designated_partition(topic)
    # kafka_ins.async_produce_message(topic)
    kafka_ins.get_produce_message_report(topic)


