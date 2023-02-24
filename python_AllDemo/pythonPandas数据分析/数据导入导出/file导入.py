'''txt文件导入'''
from pandas import read_table

df = read_table(r'D:\BaiduNetdiskDownload\python\rz.txt', sep=" ")  # r代表不转义
# print(df.head())  # 默认输出前5行,路径中不能有中文
'''csv文件导入'''
from pandas import read_csv

df = read_csv(r'D:\BaiduNetdiskDownload\python\rz.csv', sep=",")
'''excel文件导入'''
from pandas import read_excel

df = read_excel(r'D:\BaiduNetdiskDownload\python\i_nuc.xls', sheet_name='Sheet3')
'''数据库导入'''
import pymysql
import pymysql.cursors
import pandas as pd

dbconn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders', charset='utf8')
sqlcmd = "select * from students"
a = pd.read_sql(sqlcmd, dbconn)
print(a.head())
dbconn.close()

