import requests
import json
from bs4 import BeautifulSoup


url = "http://www.win4000.com/zt/ribendongman_1.html"
#获取需要爬取的内容网址--这是我需要爬取的深圳
headers = {
	"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
}
#爬虫的用户信息
response = requests.get(url, headers=headers)
print(response.text)
#获取连接,传入连接和
text = response.text
#使用requests的属性把爬取到的内容转换为utf8的格式,现在获得到的是整个页面的源代码
