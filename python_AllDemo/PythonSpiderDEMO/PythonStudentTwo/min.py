
import pymysql


def connect():
	conn = pymysql.connect(
		host='localhost',
		port=3306,
		user='root',
		password='root',
		database='pythonone',
		charset='utf8'
	)
	cursor = conn.cursor()
	sql = "INSERT INTO pythonone (title,optionl,answer)VALUES('%s','%s','%s')"
	data = ('4', '2', '3')
	cursor.execute(sql % data)
	conn.commit()
	print('成功插入', cursor.rowcount, '条数据')
	conn.close()
	cursor.close()

if __name__ == '__main__':
	connect()

