# 账户,营业额,花费,日期
import random
import time


def create_data(data):
	with open("data2.txt", "a+", encoding='UTF-8') as fp:
		fp.writelines(data + "\n")


def create_date():
	a1 = (2014, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
	a2 = (2018, 3, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）

	start = time.mktime(a1)  # 生成开始时间戳
	end = time.mktime(a2)  # 生成结束时间戳

	# 随机生成10个日期字符串
	for i in range(1):
		t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
		date_touple = time.localtime(t)  # 将时间戳生成时间元组
		date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）

		return date


def create_data_txt():
	str = ["zhangsan@163.com", "lisi@163.com", "wangwu@126.com", "liushihao@qq.com", "dage@163.com"]
	rand = random.randint(0, 4)
	df_str = str[rand]
	business = random.randint(0, 20) * 1000
	business2 = random.randint(0, 20) * 1000
	strin = "{} {} {} {}"
	pv = strin.format(df_str,business,business2,create_date())
	return pv


if __name__ == '__main__':
	for i in range(1000):
		pv=create_data_txt()
		create_data(pv)
