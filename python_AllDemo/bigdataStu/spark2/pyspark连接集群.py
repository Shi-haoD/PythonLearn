
from pyspark.sql import SparkSession
spark = SparkSession \
        .builder \
        .enableHiveSupport() \
        .master("spark://192.168.104.176:7077") \
        .appName("my_first_app_name") \
        .getOrCreate()
print(spark)