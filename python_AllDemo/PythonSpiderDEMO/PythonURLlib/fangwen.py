import json
import random
import time


def save_data(data):
	with open("fangwen7.txt", "a+", encoding='UTF-8') as fp:
		# json.dump(data, fp, ensure_ascii=False, indent=4)
		fp.writelines(data + "\n")


def shijian(cishu):
	a1 = (2018, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
	a2 = (2018, 3, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）

	start = time.mktime(a1)  # 生成开始时间戳
	end = time.mktime(a2)  # 生成结束时间戳

	# 随机生成10个日期字符串
	for i in range(cishu):
		t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
		date_touple = time.localtime(t)  # 将时间戳生成时间元组
		date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）

		return date


def shengcheng1(cishu1):
	suiji = ""
	for i in range(cishu1):
		sui1 = random.randint(1, 225)
		sui2 = random.randint(200, 800)
		sui3 = random.randint(1, 20)
		day = random.randint(1, 3)
		suijjj = random.randint(0, 2)
		cishu1 = shijian(1)
		wangzhi = ["www.baidu.com", "www.sina.com", "www.bilibili.com"]

		wangzhisuiji = wangzhi[suijjj]
		str = '8.35.201.{}--[{}/May/{} +8000 "{}"{}]'
		str2 = '2018-08-{} 12:14:59 index_v http://192.168.{}.{}:41001'
		suiji2 = str2.format(day, sui3, sui1)
		suiji = str.format(sui1, day, cishu1, wangzhisuiji, sui2)
		print(suiji2)
		save_data(suiji2)


if __name__ == '__main__':
	shengcheng1(500000)
