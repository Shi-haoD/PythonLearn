# import requests
'''返回相应的请求信息 '''
# data={
# 	'name':'liu',
# 	'age':'20'
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

'''抓取网页'''
# import requests
# import re
#
# headers={
# 	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,r.text)
# print(titles)
# ['\n为什么同样都是为大宋议和，寇准就是英雄，秦桧就是奸人呢？\n', '\n各位是否想过防弹曾经可能要解散？\n', '\n如何看待曾国藩被部分人誉为「古今第一完人」？\n', '\n如何评价《香蜜沉沉烬如霜》里的神魔大战？\n', '\n2019年中国航天会有哪些值得关注的发射任务？\n', '\n如何评价《海贼王》第925话？\n', '\n怎样看待华晨宇说自己做音乐的天赋占百分之九十九，努力占百分之一？\n', '\n你觉得《三体》中最残忍的一句话是什么？\n', '\n什么时候你觉得家长对抑郁症的理解很少？\n', '\n人类有哪些细思恐极的事？\n']

'''抓取二进制文件,图片音频视频'''
# import requests
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)#打开github文件的二进制,并且保存成文件
# with open('facicon.ico','wb')as f:
# 	f.write(r.content)

'''post请求'''
# import requests
# data={'name':'liu','age':'20'}
# r = requests.post('http://httpbin.org/post',data=data)#相关信息返回
# print(r.text)

'''响应'''
import requests
r = requests.get('https://www.jianshu.com')
print(type(r.status_code),r.status_code)#状态
print(type(r.headers),r.headers)#响应头
print(type(r.cookies),r.cookies)#cookies
print(type(r.url),r.url)#url
print(type(r.history),r.history)#请求历史
