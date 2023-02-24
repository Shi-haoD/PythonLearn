import pymysql
import requests
from bs4 import BeautifulSoup
from pyecharts import Pie
import string
import json
'''
1爬取网页的所有p标签信息
2分类p标签  3 - 9 - 15是标题
		   4 5 6 7,10 11 12 13是答案 ABCD
		   8 - 14 - 20 是正确答案
3分类存储数据到数据库
'''
psq = []

conn = pymysql.connect(
	host='localhost',
	port=3306,
	user='root',
	password='root',
	database='pythonone',
	charset='utf8'
)
cursor = conn.cursor()


def get_page(url):
	headers = {
		"User-Agent":
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
	}

	response = requests.get(url, headers=headers)
	text = response.content.decode("gb2312")
	soup = BeautifulSoup(text, 'lxml')
	# 拿到每个网页的题目内容

	newsArea = soup.find('div', class_='newsArea-2nd-PageWord')
	ps = newsArea.find_all('p')
	ps = ps[2:-2]
	for index in range(0, len(ps)):

		if index % 6 == 0 or index == 0:
			ps1 = ps[index]
		if index % 6 == 1 or index == 1:
			psa = ps[index]

		if index % 6 == 2 or index == 2:
			psb = ps[index]

		if index % 6 == 3 or index == 3:
			psc = ps[index]

		if index % 6 == 4 or index == 4:
			psd = ps[index]

		if index == 5 or index % 6 == 5:
			ps3 = ps[index]
		# sql = "INSERT INTO pythonone (title,optionla,optionlb,optionlc,optionld,answer)VALUES('%s','%s','%s','%s','%s','%s')"
		# data = (ps1, psa, psb, psc, psd, ps3)
		# cursor.execute(sql % data)
		# print('成功插入', cursor.rowcount, '条数据')
		# conn.commit()
		'''
		数据库存储
		'''


# V=[]
# atter = ['A', 'B', 'C', 'D']
# pie = Pie('答题分析图', title_pos='center', width=1000)
# pie.add("答案分析",atter,V,center=[75,50],is_random=True,radius=[30,75],rosetype='area',is_more_utils=True,is_legend_show=False,is_label_show=True)
# pie.render('ss.html')
res = {}


def analyze(get_row):
	# 传进来一个元组
	for s in get_row:  # 分行读取
		ss = "".join(s)  # 转换字符串(有换行)
		print(ss.replace('\r\n', " "))

	for i in ss:
		# 读取字符串中每个字符出现的次数
		res[i] = res.get(i, 0) + 1
	# 只能读取一行
	print(res)


def select_mysql():
	mysqlFirst = conn.cursor()
	sql = 'SELECT answer FROM pythonone'
	mysqlFirst.execute(sql)
	mysqlFirst.rowcount
	get_row = mysqlFirst.fetchall()
	print(type(get_row))
	analyze(get_row)
	conn.close()
	cursor.close()


def mian():
	urls = [
		'http://www.233.com/chengkao/zzhenti/zhengzhi/201612/27170910935.html',
		'http://www.233.com/chengkao/zzhenti/zhengzhi/201612/27151830356.html',
		'http://www.233.com/chengkao/zzhenti/zhengzhi/201612/27151302672.html'
	]
	for url in urls:
		get_page(url)


def save_data(data):
	with open("dainying.json", "a+", encoding='UTF-8') as fp:
		json.dump(data, fp, ensure_ascii=False, indent=4)


if __name__ == '__main__':
	mian()
	select_mysql()
