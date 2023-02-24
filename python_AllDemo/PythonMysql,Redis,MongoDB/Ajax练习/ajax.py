from urllib.parse import urlencode
import requests

base_url = "https://m.weibo.cn/api/container/getIndex?"

headers = {
	'Host': 'm.weibo.cn',
	'Referer': 'https://m.weibo.cn/u/5779946643',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
	'X-Request-With': 'XMLHttpRequest'
}


def get_pages(page):
	params = {
		'type': 'uid',
		'value': '5779946643',
		'containerid': '1076035779946643',
		'page': page
	}
	url = base_url + urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError as e:
		print(e.args)


# 上面定义了请求需要的url,并且看看能否通过

# 下面解析几个内容
from pyquery import PyQuery as pq


def parse_page(json):
	if json:
		items = json.get('data').get('cards')
		for item in items:
			item = item.get('mblog')
			weibo = {}
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitudes'] = item.get('attitudes_count')
			weibo['comments'] = item.get('comments_count')
			weibo['reposts'] = item.get('reposts_count')

			yield weibo


from pymongo import MongoClient

client = MongoClient()
db = client['weibo']
collention = db['weibo']


def save_to_mogo(result):
	if collention.insert(result):
		print('saved')


if __name__ == '__main__':
	for page in range(1, 11):
		json = get_pages(page)
		results = parse_page(json)
		for result in results:
			print(result)
			save_to_mogo(result)
