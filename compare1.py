import pyspark
from pyspark.sql import SparkSession
import pandas as pd
import time

spark = SparkSession.builder.appName("readcsv").getOrCreate()
health_df_pyspark = spark.read.csv(path="health care diabetes.csv",sep=",",header=True,inferSchema=True)

health_df_pandas = pd.read_csv('health care diabetes.csv')

start_pd = time.time()
health_df_pandas.describe()
end_pd  = time.time()
print("The time of execution of pandas program is :", end_pd-start_pd)

start_ps = time.time()
health_df_pyspark.describe()
end_ps = time.time()
print("The time of execution of pyspark program is :", end_ps-start_ps)

