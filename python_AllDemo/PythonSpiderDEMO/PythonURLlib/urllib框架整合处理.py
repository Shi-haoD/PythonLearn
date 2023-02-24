import urllib.request
import socket
import urllib.error

# response = urllib.request.urlopen("https://www.python.org/")#爬取网页
'''urllib框架的基本用法'''
#
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

'''data参数'''
#
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())
# #?????输出为什么又\n

'''timeout参数(try - except)'''
#
# try:
# 	response = urllib.request.urlopen('http://httpbin.org/post',timeout=0.1)#设置超时
# except urllib.error.URLError as e:
# 	if isinstance(e.reason,socket.timeout):
# 		print('timeout')
'''request方法'''
#
# request = urllib.request.Request("https://www.python.org/")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
'''
添加代理
'''
# 	'http':'http://127.0.0.1:9743',
# 	#添加了连个9743代理端口
# 	'https':'https://127.0.0.1:9743'
# })
# opener = build_opener(Proxy_handler)
# try:
# 	reponse = urllib.request.urlopen("https://www.baidu.com")
# 	print(reponse.read().decode('utf-8'))
# except URLError as e:
# 	print(e.reason)
#
# from urllib.error import URLError
# from urllib.request import ProxyHandler , build_opener
#
# from more_itertools import bucket
#
# Proxy_handler = ProxyHandler({

'''
cookies的获取
##需要使用相关的方法
'''
# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print(item.name + "=" + item.value)
'''
生成text文件,cookie的信息
'''
#
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)    LWPCookieJar 保存Lwp格式的文件
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

'''
读取文本地的lwp的文件内容,来查看网页源代码,上边已经生成了lwp文件
'''
# cookie = http.cookiejar.LWPCookieJar()
# # cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
# # handler = urllib.request.HTTPCookieProcessor(cookie)
# # opener = urllib.request.build_opener(handler)
# # response = opener.open('http://www.baidu.com')
# # print(response.read().decode('utf-8'))

'''异常处理'''
# from urllib import request, error
# try:
# 	response = request.urlopen("https://cuiqingcai.com/index.html")
# except error.URLError as e:
# 	print(e.reason,e.code,e.headers,sep='\n')
'''异常处理2,先捕获父类异常'''
# from urllib import request,error
# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.html')
# except error.HTTPError as e1:#先捕获父类
# 	print(e1.reason,e1.code,e1.headers)
# except error.URLError as e2:
# 	print(e2.reason)
# else:
# 	print('没有异常')
'''异常处理3,超时异常处理'''
# import socket
# import urllib.request
# import urllib.error
#
# try:
# 	response = urllib.request.urlopen('https://www.baidu.com',timeout=0.1)
# except urllib.error.URLError as e:
# 	print(type(e.reason))#输出一个 timeout的类
# 	if isinstance(e.reason,socket.timeout):
# 		print('time out ')
'''解析连接'''