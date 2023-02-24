import requests
from urllib.parse import urlencode
from hashlib import md5
import os
from multiprocessing.pool import Pool
from requests import codes


def get_pages(offset):
	params = {
		'offset': offset,
		'format': 'json',
		'keyword': '美女',
		'autoload': 'true',
		'count': '20',
		'cur_tab': '1',
		'from': 'seach_tab'
	}
	url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
	# base_url = 'https://www.toutiao.com/search_content/?'
	# url = base_url + urlencode(params)
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError:
		return None


def get_images(json):
	if json.get('data'):
		data = json.get('data')
		for item in data:
			if item.get('cell_type') is not None:
				print('1')
				continue
			title = item.get('title')
			images = item.get('image_list')
			for image in images:
				yield {
					'image': 'https:' + image.get('url'),
					'title': title
				}


def save_image(item):
	# if not os.path.exists(item.get('title')):
	# 	os.mkdir(item.get('title'))
	# try:
	# 	response = requests.get(item.get('image'))
	# 	if response.status_code == 200:
	#
	# 		print(response.status_code)
	# 		file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
	# 		if not os.path.exists(file_path):
	# 			with open(file_path, 'wb') as f:
	# 				f.write(response.content)
	# 			print('Downloaded image path is %s' % file_path)
	# 		else:
	# 			print('Already Downloaded', file_path)
	# except requests.ConnectionError:
	# 	print('Failed to Save Image，item %s' % item)
	img_path = 'img' + os.path.sep + item.get('title')
	if not os.path.exists(img_path):
		os.makedirs(img_path)
	try:
		resp = requests.get(item.get('image'))
		if codes.ok == resp.status_code:
			file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
				file_name=md5(resp.content).hexdigest(),
				file_suffix='jpg')
			if not os.path.exists(file_path):
				with open(file_path, 'wb') as f:
					f.write(resp.content)
				print('Downloaded image path is %s' % file_path)
			else:
				print('Already Downloaded', file_path)
	except requests.ConnectionError:
		print('Failed to Save Image，item %s' % item)


def main(offset):
	json = get_pages(offset)
	for item in get_images(json):
		print(item)
		save_image(item)


GROUP_START =0
GROUP_END = 50

if __name__ == '__main__':
	pool = Pool()
	groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
	pool.map(main, groups)
	pool.close()
	pool.join()
