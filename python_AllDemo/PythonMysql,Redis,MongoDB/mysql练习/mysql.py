# import pymysql
'''使用mysql数据库'''
# db = pymysql.connect(host = 'localhost',user='root',password='root',port=3306)
# #连接数据库
# cursor = db.cursor()#创建操作游标
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print('version',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursot=db.cursor()
# data = {
# 	'id': '20120001',
# 	'name':'刘世豪',
# 	'age': '20',
#
# }
# table = 'students'
# keys = ','.join(data.keys())
# values= ','.join(['%s']*len(data))
# sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try :
# 	if cursot.execute(sql,tuple(data.values())):
# 		print('成功插入')
# 		db.commit()
# except:
# 	print('失败')
# 	db.rollback()
# db.close()
# import pymysql
# db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
# currsor = db.cursor()
# sql = 'SELECT * FROM students WHERE age>=20'
# try:
# 	currsor.execute(sql)
# 	print(currsor.rowcount)
# 	first = currsor.fetchone()
# 	print(first)
# 	all = currsor.fetchall()
# 	print(all)
# 	print(type(all))
# 	for i in all:
# 		print(i)
# except:
# 	print('拆线呢十八')
