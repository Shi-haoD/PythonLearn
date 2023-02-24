import pymongo

con = pymongo.MongoClient(host='localhost', port=27017)
db = con.test
collection = db.students
# mongoDB非关系数据库存储
student = {
	'id': '20181221',
	'name': '刘世豪',
	'age': '20',
	'gender': 'nan'
}
student1 = {
	'id': '20181221',
	'name': '林法扬',
	'age': '21',
	'gender': 'nan'
}
student2 = {
	'id': '20181221',
	'name': '王雪陈',
	'age': '22',
	'gender': 'nan'
}
'''插入数据单条或者列表多条数据插入'''
#result = collection.insert(student)#插入数据单条或者列表多条数据插入
'''插入数据,多条数据插入'''
result = collection.insert_many([student1,student2])#插入数据,多条数据插入
'''查询单条数据'''
result = collection.find_one({'name':'王雪陈'})#查询单条数据
'''查询多条语句然后需要循环遍历出来'''
# result = collection.find({'age':'20'})#查询多条语句然后需要循环遍历出来
# for i in result:
# 	print(i)
'''大于等于20碎'''
# results = collection.find({'age':{'$gte':'20'}})#大于等于20碎
# for i in results:
# 	print(i)
'''计数查询有几个符合条件的'''
# count = collection.find().count()#查询全部数据
# count = collection.find('age':'20').count()#查询符合条件的数据
# print(count)
'''排序'''
# results = collection.find().sort('name',pymongo.DESCENDING)#升序标志ASCENDING升序   DESCENDING倒叙
# print([result['name'] for result in results])
'''偏移'''
# results = collection.find().sort('age',pymongo.ASCENDING).skip(0)#SKIP往后数几个
# print([result['age'] for result in results])
'''设置提取个数'''
# results = collection.find().sort('name',pymongo.DESCENDING).limit(2)#limit设置取几个
# print([result['name'] for result in results])
'''修改名字为刘世豪的 条目为刘世豪大帅哥'''
# condition = {'name':'刘世豪'}#徐晓修改的字段
# student = collection.find_one(condition)
# student['name'] = '大帅哥刘世豪'
# result = collection.update(condition,student)
# print(result)
'''年龄大于20的增加1'''
# condition = {'age': {'$gte':20}}#大于等于20
# result = collection.update_one(condition, {'$inc': {'age': 1}})#增加1,只会增加第一个update_many可以修改全部符合条件的
print(result)
# print(result.matched_count)#匹配条数
# print(result.modified_count)#影响条数


