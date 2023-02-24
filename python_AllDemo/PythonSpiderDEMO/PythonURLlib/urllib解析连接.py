
'''解析连接1urlparse'''
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)#<class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# #解析了一个url

'''解析连接2 urlunparse'''
# from urllib.parse import urlunparse
# data = ['http','www.baidu.comm','index.html','user','a=6','comment']#http://www.baidu.comm/index.html;user?a=6#comment
# print(urlunparse(data))#拼接成了一个连接实现了url构造

'''解析连接3 urlsplit'''
# from urllib.parse import urlsplit
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')#SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
# print(result)#参数合并到了 path中

'''解析连接3 urlunsplit'''
# from urllib.parse import urlunsplit
# data = ['http','www.baidu.com','index.html','a=6','comment']#http://www.baidu.com/index.html?a=6#comment
# print(urlunsplit(data))#反拼一个url

'''解析连接4 urljoin 字符串拼接成一个完整的url'''
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','http://cuiqingcai/FAQ.html'))
print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html?question=2'))