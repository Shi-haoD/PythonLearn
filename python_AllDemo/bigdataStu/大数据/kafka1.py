from pykafka import KafkaClient
import time


class KafaTest(object):
	'''
	api 测试
	'''

	def __init__(self, host="192.168.104.176:9092"):
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


if __name__ == '__main__':
	host = '192.168.104.176:9092,192.168.104.174:9092'
	kafka_ins = KafaTest(host)
	print(kafka_ins)
	topic = 'mytopic1'
	kafka_ins.producer_partition(topic)
