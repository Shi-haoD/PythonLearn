from pyspark import SparkContext

from pyspark import SparkContext as sc
from pyspark import SparkConf
conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
sc=SparkContext.getOrCreate(conf)
rdd = sc.parallelize([1,2,3,4,5])
rdd
print(rdd)
print(rdd.getNumPartitions())
