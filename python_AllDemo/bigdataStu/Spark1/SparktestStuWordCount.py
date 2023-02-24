
from operator import add
from pyspark import SparkContext
sc = SparkContext(appName='test1')
rdd = sc.textFile('test1').flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(add).collect()
for (word,count) in rdd:
	print(f"word:--{word},count:--{count}")
sc.stop()