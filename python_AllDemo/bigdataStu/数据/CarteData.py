import random
import time


def create_data(data):
	with open("data01.txt", "a+", encoding='UTF-8') as fp:
		fp.writelines(data + "\n")


# 手机号 -                  mac地址 -                网址域名ip -         网址 -     网站类型 -当天的上行量 - 下行量 - 访问状态码 - 日期
# 1363157985066     00-FD-07-A4-72-B8:CMCC    120.196.100.82    i02.c.aliimg.com   财经     2481    24681          200           2018-1-1
# 随机数据              随机数据					网址要对应 -  ip - 类型                       随机数据  随机数据       不用栋          随机日期


def create_mac():
	Maclist = []
	for i in range(1, 7):
		RANDSTR = "".join(random.sample("0123456789abcdef", 2))
		Maclist.append(RANDSTR)
	RANDMAC = ":".join(Maclist)
	return RANDMAC


def carte_phone():
	# 第二位数字
	second = [3, 4, 5, 7, 8][random.randint(0, 4)]

	# 第三位数字
	third = {
		3: random.randint(0, 9),
		4: [5, 7, 9][random.randint(0, 2)],
		5: [i for i in range(10) if i != 4][random.randint(0, 8)],
		7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
		8: random.randint(0, 9),
	}[second]

	# 最后八位数字
	suffix = random.randint(9999999, 100000000)

	# 拼接手机号
	return "1{}{}{}".format(second, third, suffix)


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


def create_ip():
	rand = random.randint(0, 3)
	ip = [
		["120.196.100.82","i02.c.aliimg.com","财经"],
		["120.197.40.4","sug.so.360.cn","信息安全"],
		["120.196.100.99","iface.qiyi.com","视频网站"],
		["47.95.47.253:443","blog.csdn.net","技术网站"]
	]
	ip = ip[rand]
	return " ".join(ip)


def create_rand():
	sui1 = random.randint(3000, 20000)
	return sui1


def create_joint():
	str = "{} {} {} {} {} 200 {}"
	pv = str.format(carte_phone(), create_mac(), create_ip(), create_rand(), create_rand(), create_date())

	return pv


if __name__ == '__main__':
	for i in range(1000):
		pv = create_joint()
		create_data(pv)