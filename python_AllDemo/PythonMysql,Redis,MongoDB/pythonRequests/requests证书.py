# import requests
'''证书'''
# response = requests.get('https://www.12306.cn')
# print(response.status_code)
# #这个没发生证书错误

#这个发生了警告
# import requests
# response = requests.get("https://www.12306.cn",verify=False)
# print(response.status_code)#请求成功

#忽略警告
# import requests
# import logging
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)


