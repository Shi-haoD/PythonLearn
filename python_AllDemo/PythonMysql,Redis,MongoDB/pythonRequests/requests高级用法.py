'''文件上传'''
# import requests
# files = {"file":open('facicon.ico','rb')}
# r = requests.post('http://httpbin.org/post',files=files)#放入解析处的二进制文件
# print(r.text)
# print(type(r.text))
# print(r.cookies)

'''cookies'''
# import requests
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
# 	print(key+'='+value)

'''使用自己的cookies访问网站,通过headers参数设置'''
# import requests
# headers={
# 	'Cookie':'_zap=209cc5d4-89d4-4bdf-97e1-0c0933da06bd; _xsrf=X92u2ktclEnQxs0nAU2WPfuJ7XvfEIhA; d_c0="AdDmXPSRMA6PTrY1aM7tmGkSRstw_87U9fY=|1536557655"; tst=r; __gads=ID=4cb5ef18f4b1e0bc:T=1539689759:S=ALNI_MZoM19zMb9St17ejgLby_J3QYDtUg; __utmv=51854390.100--|2=registration_date=20171214=1^3=entry_date=20171214=1; capsion_ticket="2|1:0|10:1543971327|14:capsion_ticket|44:YWVhYTZiYzJmNDhhNDkwMThlN2UxNGE5YTA3NGM2ZWQ=|78f98b347a1a5a98d52045c2f9d0b47bb254f9259af5157adc7ece1edebc3bf3"; r_cap_id="OGZlMDA4MTY1ZjdhNDcyM2EzY2U0OTRlYzc3MTM1MDA=|1543971441|01108c0f726623c4dec24a7eb27758249f359e05"; cap_id="NmI4MDRhMDk1MjQ4NDJjODg0ZWFiMjk1M2VjNzViNGU=|1543971441|5f8957b2d4be80eaf24312fd06c76aaaacab03fa"; l_cap_id="MGJlYTY3NGJlOWViNDU2Nzk5NjEzNjc0YzYyZjk4ZDk=|1543971441|ab75a2e2f63d51317f9bb7f52230b4cd64f02237"; z_c0=Mi4xVWhuaUJnQUFBQUFCME9aYzlKRXdEaGNBQUFCaEFsVk5lSEQwWEFDV1loSjBBVGtSckxkejhrSGJveGNQMU5fNFpB|1543971448|b3a9148b578b6b5a81cb23af0788ad664f78f05d; q_c1=12283420754c4d95a734410e8c70e7ff|1545033625000|1536557669000; __utma=51854390.1664571995.1541414863.1541648549.1545033630.5; __utmz=51854390.1545033630.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; tgw_l7_route=9553ebf607071b8b9dd310a140c349c5'
# 	,'Host':'www.zhihu.com',
# 	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

'''使用cookies,构造requestsCookiesJar对象'''
# import requests
# cookies = 'zap=209cc5d4-89d4-4bdf-97e1-0c0933da06bd; _xsrf=X92u2ktclEnQxs0nAU2WPfuJ7XvfEIhA; d_c0="AdDmXPSRMA6PTrY1aM7tmGkSRstw_87U9fY=|1536557655"; tst=r; __gads=ID=4cb5ef18f4b1e0bc:T=1539689759:S=ALNI_MZoM19zMb9St17ejgLby_J3QYDtUg; __utmv=51854390.100--|2=registration_date=20171214=1^3=entry_date=20171214=1; capsion_ticket="2|1:0|10:1543971327|14:capsion_ticket|44:YWVhYTZiYzJmNDhhNDkwMThlN2UxNGE5YTA3NGM2ZWQ=|78f98b347a1a5a98d52045c2f9d0b47bb254f9259af5157adc7ece1edebc3bf3"; r_cap_id="OGZlMDA4MTY1ZjdhNDcyM2EzY2U0OTRlYzc3MTM1MDA=|1543971441|01108c0f726623c4dec24a7eb27758249f359e05"; cap_id="NmI4MDRhMDk1MjQ4NDJjODg0ZWFiMjk1M2VjNzViNGU=|1543971441|5f8957b2d4be80eaf24312fd06c76aaaacab03fa"; l_cap_id="MGJlYTY3NGJlOWViNDU2Nzk5NjEzNjc0YzYyZjk4ZDk=|1543971441|ab75a2e2f63d51317f9bb7f52230b4cd64f02237"; z_c0=Mi4xVWhuaUJnQUFBQUFCME9aYzlKRXdEaGNBQUFCaEFsVk5lSEQwWEFDV1loSjBBVGtSckxkejhrSGJveGNQMU5fNFpB|1543971448|b3a9148b578b6b5a81cb23af0788ad664f78f05d; q_c1=12283420754c4d95a734410e8c70e7ff|1545033625000|1536557669000; __utma=51854390.1664571995.1541414863.1541648549.1545033630.5; __utmz=51854390.1545033630.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; tgw_l7_route=9553ebf607071b8b9dd310a140c349c5'
# jar = requests.cookies.RequestsCookieJar(cookies)
# headers={
# 	'Host':'www.zhihu.com',
# 	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
# }
# r = requests.get('http://www.zhihu.com',headers=headers,cookies=jar)
# print(r.text)

'''会话维持'''
import requests
# requests.get("http://httbin.org/cookies/set/number/123456789")
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
#这种访问并不行
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)
#这种访问可以获取到绘画维持

from requests import Request , Session
url = "http://httpbin.org/post"
data={
	'name':'germey'
}
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)