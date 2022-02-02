import pyspark
from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("readcsv").getOrCreate()

health_df = spark.read.csv(path="health care diabetes.csv",sep=",",header=True,inferSchema=True)

start = time.time()
#print(health_df.show(5))
print(health_df.describe().show())
end = time.time()
print("The time of execution of pyspark program is :", end-start)

