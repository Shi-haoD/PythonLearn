from kafka import KafkaConsumer
import pymysql

consumer = KafkaConsumer('mytopic1', bootstrap_servers=['192.168.104.176:9092'])
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursot = db.cursor()
for message in consumer:
	name = message.topic
	partition = message.partition
	offset = message.offset
	key1 = message.key
	values = message.value
	print(values)
	valuess = str(values, encoding="utf8")
	values1=valuess.split(" ")
	values2= values1[8].strip("\n").strip("\r")
	print(values1[8].strip("\n").strip("\r"))
	print(values1[1])
	data = {
		'name': name,
		'partition': partition,
		'offset': offset,
		'key1': values1[1],
		'valuesv':values2
	}

	table = 'log'
	keys = ','.join(data.keys())
	values = ','.join(['%s'] * len(data))

	sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
	try:
		db.ping(reconnect=True)

		if cursot.execute(sql, tuple(data.values())):
			print('成功插入')
			db.commit()
	except:
		print('失败')
		db.rollback()
	db.close()
