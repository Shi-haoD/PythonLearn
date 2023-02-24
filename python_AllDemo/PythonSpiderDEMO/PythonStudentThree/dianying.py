import requests
from lxml import etree
import time
import pymysql
import json

conn = pymysql.connect(
	host='localhost',
	port=3306,
	user='root',
	password='root',
	database='python1',
	charset='utf8'
)
cursor = conn.cursor()

Headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
}
BASE_DOMAIN = 'https://www.dytt8.net'

MAX_RETRIES = 20


def get_detail_urls(url):
	# 创建爬虫

	response = requests.get(url, headers=Headers)
	text = response.text
	html = etree.HTML(text)
	detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
	detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
	return detail_urls


def parse_detail_page(url):
	# 解析url
	response = requests.get(url, headers=Headers)
	movie = {}
	text = response.content.decode('gbk')
	html = etree.HTML(text)
	# 获取标题
	title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
	# 标题存入列表
	movie['title'] = title
	movie11 = movie['title']
	movie11s = "".join(movie11)
	# 拿到主内容的div
	if html.xpath("//div[@id='Zoom']")[0] != None:
		zoomE = html.xpath("//div[@id='Zoom']")[0]
	# 拿到海报和下面的电影截图
	images = zoomE.xpath(".//img/@src")
	# 拿到海报

	# 拿到截图
	cover = images[0]
	screenshot = images[1]
	movie['screenshot'] = screenshot
	movie['cover'] = cover

	# 拿到内容
	infos = zoomE.xpath('//text()')

	def prase_info(info, rule):
		# 定义规则
		return info.replace(rule, '').strip()

	for index, info in enumerate(infos):
		if info.startswith('◎年　　代'):
			info = prase_info(info, '◎年　　代')
			movie['years'] = info
			movie1 = movie['years']
		elif info.startswith('◎产　　地'):
			info = prase_info(info, '◎产　　地')
			movie['address'] = info
			movie2 = movie['address']
		elif info.startswith('◎类　　别'):
			info = prase_info(info, '◎类　　别')
			movie['kind'] = info
			movie3 = movie['kind']
		elif info.startswith('◎上映日期'):
			info = prase_info(info, '◎上映日期')
			movie['day'] = info
			movie4 = movie['day']
		elif info.startswith('◎IMDb评分'):
			info = prase_info(info, '◎IMDb评分')
			movie['source'] = info
			movie5 = movie['source']
		elif info.startswith('◎豆瓣评分'):
			info = prase_info(info, '◎豆瓣评分')
			movie['douban'] = info
			movie6 = (movie['douban'])
			movie6s = movie6.replace(" ' ", " ")
		elif info.startswith('◎导　　演'):
			info = prase_info(info, '◎导　　演')
			movie['director'] = info
			movie7 = movie['director']
		elif info.startswith('◎主　　演'):
			info = prase_info(info, '◎主　　演')
			actors = []
			for x in range(index + 1, len(infos)):
				actor = infos[x].strip().replace("'", " ")
				if actor.startswith('◎'):
					break
				actors.append(actor)
			movie['actors'] = actors
			movie8 = movie['actors']
			movie8s = "".join(movie8).replace("'", " ")
		elif info.startswith('◎简　　介'):
			info = prase_info(info, '◎简　　介')
			introduces = []
			for x2 in range(index + 1, len(infos)):
				introduce = infos[x2].strip()
				if introduce.startswith('【下载地址】'):
					break
				introduces.append(introduce)
			movie['introduce'] = introduces
	dowlnoad_url = html.xpath('//td[@bgcolor="#fdfddf"]/a/@href')[0]
	movie['dowlnoad_url'] = dowlnoad_url
	movie9 = movie['dowlnoad_url']

	# sql = "INSERT INTO dianying (title,years,address,kind,`day`,source,douban,director,actors,introduce)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
	# 	movie11s, movie1, movie2, movie3, movie4, movie5, movie6s, movie7, movie8s, movie9)
	# data = (pymysql.escape_string(movie1), pymysql.escape_string(movie2), pymysql.escape_string(movie3), pymysql.escape_string(movie4), pymysql.escape_string(movie5), pymysql.escape_string(movie6),pymysql.escape_string(movie7),pymysql.escape_string(movie8),pymysql.escape_string(movie9))
	# data = (movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9)
	# cursor.execute(sql)
	# print('成功插入', cursor.rowcount, '条数据')
	# conn.commit()
	return movie


def spider():
	# 生成ur`w
	base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
	movies = []
	for x in range(6, 25):
		# 第一个for控制循环多少页`
		url = base_url.format(x)
		detail_urls = get_detail_urls(url)
		for dateil_url in detail_urls:
			print("当前位置", x, "的", dateil_url)
			# 遍历每页中的详情url
			movie = parse_detail_page(dateil_url)
			movies.append(movie)
			time.sleep(11)
			print(movies[-1])
			save_data(movies[-1])


# !/usr/bin/env python
# -*- coding: UTF-8 -*-
def save_data(data):
	with open("dainying4.json", "a+", encoding='UTF-8') as fp:
		json.dump(data, fp, ensure_ascii=False)
		fp.writelines("\n")


if __name__ == '__main__':
	spider()
