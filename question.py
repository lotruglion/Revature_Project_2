from ast import expr
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import pandas as pd
from pyspark import SparkContext, sql, SparkConf
from pyspark.sql import SparkSession, Row, HiveContext, SQLContext
import pyspark
from pyspark.sql.functions import col
import os
import sys
import pyspark.sql.functions 



#Pyspark test code for dataframe creation
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession\
    .builder\
    .appName("Project_2")\
    .master("local[*]")\
    .getOrCreate()

sc = spark.sparkContext
sqlcontext = SQLContext(spark)
df_pyspark=spark.read.option('header', 'true').csv('backup.csv')
#df_pyspark.select("product_name").show()
#question 1
#df_pyspark.select("product_category","country", "qty").groupBy("country", "product_category").agg({"qty":"sum"}).show()
#question 3
df_pyspark.select("qty","city","country").groupBy("country","city").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).show()
#question 4
df_pyspark.select("qty","datetime").groupBy("datetime").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).show()
df_pyspark.select("qty","datetime","country").groupBy("country","datetime").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).drop_duplicates(["country"]).show()