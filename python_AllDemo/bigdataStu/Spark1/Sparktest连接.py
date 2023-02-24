import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext


se = SparkSession.builder.config(conf=pyspark.SparkConf()).getOrCreate
sc = SparkContext(appName='Student')
sq = SparkSession.builder.getOrCreate

user = sc.textFile("test1.txt")
