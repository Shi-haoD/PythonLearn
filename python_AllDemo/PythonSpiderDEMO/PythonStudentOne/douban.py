import requests
import json
from bs4 import BeautifulSoup


def get_page():
	url = "https://movie.douban.com/cinema/nowplaying/shenzhen/"
	#获取需要爬取的内容网址--这是我需要爬取的深圳
	headers = {
		"User-Agent":
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
	}
	#爬虫的用户信息
	response = requests.get(url, headers=headers)
	#获取连接,传入连接和
	text = response.text
	#使用requests的属性把爬取到的内容转换为utf8的格式,现在获得到的是整个页面的源代码
	return text


def parse_page(text):
	soup = BeautifulSoup(text, 'lxml')
	print(soup)
	#使用beautifulsoup的解析库 把得到html内容解析成一个个对象放在对象集合中{'li':'1'}
	moves = []
	liList = soup.find_all("li", attrs={"data-category": "nowplaying"})
	#这是拿到所有的li标签中data-category属性值为nowplaying的标签的一整个li
	for li in liList:
		#下面是分析网页
		move = {}
		title = li['data-title']
		#比如这一行就是我们需要爬取的电影标题
		score = li['data-score']
		img = li.find('img')
		firstPhoto = img['src']
		move['title'] = title
		move['score'] = score
		move['firstPhoto'] = firstPhoto
		moves.append(move)
		save_data(moves[-1])
		#print(moves[-1])
	return moves


def save_data(data):
	#这个方法是把我得到的集合主内容全部放入一个json的文件中
	with open("shenzhen.json", "a+", encoding='utf-8') as fp:
		json.dump(data, fp, ensure_ascii=False)
		fp.writelines("\n")


if __name__ == '__main__':
	text = get_page()
	moves = parse_page(text)



