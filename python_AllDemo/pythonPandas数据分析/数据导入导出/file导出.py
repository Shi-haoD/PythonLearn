from pandas import DataFrame
from pandas import Series

df = DataFrame({'age': Series([30, 20, 12]), 'name': Series(['lin', 'liu', 'wang'])})
# 构造一个dataframe的函数

df.to_csv(r'F:\PythonPage\pythonPandas数据分析\数据导入导出\01.csv')
# 导出成csv的格式的文件,默认有index 如果在参数里面设置{index = False}就没有编号了
df.to_excel(r'F:\PythonPage\pythonPandas数据分析\数据导入导出\01.xlsx')
# 导出成excel文件的格式,和csv相同


'''导出到数据库'''
from sqlalchemy import create_engine

# 启动引擎
engine = create_engine("mysql+pymysql://root:root@localhost:3306/spiders?charset=utf8")

df1 = DataFrame({'age': Series([30, 20, 12]), 'name': Series(['lin', 'liu', 'wang'])})

df.to_sql(
	name='test1',
	con=engine,
	if_exists='append',
	index=False,
	index_label=False
)


