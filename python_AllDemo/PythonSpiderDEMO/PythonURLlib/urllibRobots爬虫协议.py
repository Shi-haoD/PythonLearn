from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
import urllib
"""
第一个判断
"""
# us = RobotFileParser()
# us.set_url("http://www.jianshu.com/robots.txt")#得到爬虫协议的robots文件
# us.read()#分析文件
# print(us.can_fetch('*',"http://www.jianshu.com/p/b67554025d7d"))#判断网页是否可以爬取
# print(us.can_fetch('*',"http://www.jianshu.com/search?q=pthon&page=1&type=collections"))

"""第二种"""
rp = RobotFileParser()
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"
}
rpq = urllib.request.Request(url='http://www.jianshu.com/robots.txt',headers=headers)
rp.parse(urlopen(rpq).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*',"http://www.jianshu.com/p/b67554025d7d"))#判断网页是否可以爬取
print(rp.can_fetch('*',"http://www.jianshu.com/search?q=pthon&page=1&type=collections"))