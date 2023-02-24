import requests
# 网络协议请求处理库
from bs4 import BeautifulSoup
# 从网页抓取数据
from pyecharts import Pie
import json
import re

# 数据分析 图形处理
ALL_DATA = []


def parse_page(url):
	headers = {
		"User-Agent":
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
	}
	response = requests.get(url, headers=headers)
	text = response.content.decode("utf-8")

	soup = BeautifulSoup(text, 'html5lib')
	# 提取网页全部内容

	conMidtab = soup.find('div', class_="conMidtab")
	# 把网页的class=conMidtab过滤出来(得到全部天气)一天
	tables = conMidtab.find_all('table')
	# 拿到他下面的table(拿到各个城市的天气)省里全部
	for table in tables:

		trs = table.find_all('tr')[2:]
		# 拿到table 下面全部的tr(拿到各个省内的市所有天气[2:]从第二个开始打印
		for index, tr in enumerate(trs):
			tds = tr.find_all('td')
			# 获取全部td
			city_td = tds[0]
			if index == 0:
				city_td = tds[1]
			city = list(city_td.stripped_strings)[0]
			temp_td = tds[-2]
			temp_td2 = tds[-5]
			if index == 0:
				city_a = tds[0]
			min_temp = list(temp_td.stripped_strings)[0]
			max_temp = list(temp_td2.stripped_strings)[0]
			city_All = list(city_a.stripped_strings)[0]

			ALL_DATA.append({"city": city, "min_temp": int(min_temp),"max_temp":int(max_temp), "sheng": city_All})
			print(ALL_DATA[-1])
			save_data(ALL_DATA[-1])


# 得到数据


def mian():
	urls = ['http://www.weather.com.cn/textFC/hb.shtml',
			'http://www.weather.com.cn/textFC/db.shtml',
			'http://www.weather.com.cn/textFC/hd.shtml',
			'http://www.weather.com.cn/textFC/hn.shtml',
			'http://www.weather.com.cn/textFC/gat.shtml',
			'http://www.weather.com.cn/textFC/xn.shtml',
			'http://www.weather.com.cn/textFC/xb.shtml',
			'http://www.weather.com.cn/textFC/gat.shtml']
	for url in urls:
		parse_page(url)

	ALL_DATA.sort(key=lambda data: data['min_temp'])  # 给数据输出

	data = ALL_DATA[0:10]
	# pyecharts
	cities = list(map(lambda x: x['city'], data))
	temps = list(map(lambda x: x['min_temp'], data))

	chart = Pie("中国天气最低温排行榜")
	chart.add('', cities, temps, is_more_utils=True)
	chart.render('temperature.html')


def save_data(data):
	with open("wendu2.json", "a+", encoding='UTF-8') as fp:
		json.dump(data, fp,ensure_ascii=False)
		fp.writelines("\n")


if __name__ == '__main__':
	mian()
