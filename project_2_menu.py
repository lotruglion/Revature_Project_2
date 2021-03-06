import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import pyspark
import pandas as pd
from pyspark import SparkContext, sql, SparkConf
from pyspark.sql import SparkSession, Row, HiveContext, SQLContext
import pyspark
from pyspark.sql.functions import col
import os
import sys



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
df_pyspark=spark.read.option('header', 'true').csv('ecom.csv')





#Functions that will display data frames
def consumerData():
    df_pyspark.show()

def topSelling():
    df_pyspark.select("product_category","country", "qty").groupBy("product_category").agg({"qty" : "sum"}).sort("sum(qty)", ascending =False).show()

def topSellingCountry():
    df_pyspark.select("product_category","country", "qty").groupBy("country", "product_category").agg({"qty" : "sum"}).sort("sum(qty)", ascending =False).drop_duplicates(["country"]).show()

def popularityChange():
    df_pyspark.select("product_category", "qty", "datetime").groupBy("product_category", "datetime").agg({"qty" : "sum"}).sort("datetime", ascending =True).show(100)

def popularityChangeCountry():
    df_pyspark.select("product_category","country", "qty", "datetime").groupBy("country", "product_category", "datetime").agg({"qty" : "sum"}).sort("datetime", ascending =True).show(100)

def highestSalesLocation():
    df_pyspark.select("qty","city","country").groupBy("country","city").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).show()

def highestTraffic():
    df_pyspark.select("qty","datetime").groupBy("datetime").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).show()

def highestTrafficCountry():
    df_pyspark.select("qty","datetime","country").groupBy("country","datetime").agg({"qty":"sum"}).sort("sum(qty)", ascending =False).drop_duplicates(["country"]).show()



#Menu that users will interact with
def startup():
    while True:
        print("Wholesale International Food")
        print("By Nick, Rose, Riley, and JiaYing")
        print('Please input an option from the menu:')
        print('\t1. View Consumer Data gathered within the last two years')
        print('\t2. View top selling caregory of products')
        print('\t3. View top selling category of products per Country')
        print('\t4. View how the popularity of products changes throughout the year')
        print('\t5. View how the popularity of products changes through the year by country')
        print('\t6. View which locations have the highest sales')
        print('\t7. View What times have the highest traffic of sales')
        print('\t8. View what times have the highest traffic of sales per country')
        print('\t9. Exit')
        break   
    while True:
        try:
            sel = int(input("\nSelection: "))  
        except ValueError:
            print(ValueError)
            print("Not valid input")
        else:
            break
    while True:
        if sel == 1:
            print("Data gathered from consumers over the last two years:")
            consumerData()
            print("Would you like to make another selection?")
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))    
        elif sel == 2:
            print("Here is the overall top selling categories of products:")
            topSelling()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: ")) 
        elif sel == 3:
            print("Here is the top selling categories of products by country:")
            topSellingCountry()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 4:
            print("Here's the changes in popularity with products through the year:")
            popularityChange()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 5:
            print("Here's how popularity with products changes through the year by country:")
            popularityChangeCountry()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year.')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 6:
            print("Here are the highest sales by location:")
            highestSalesLocation()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t7. View What times have the highest traffic of sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 7:
            print("Here are the times with the highest traffic of sales:")
            highestTraffic()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t8. View what times have the highest traffic of sales per country')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 8:
            print("Here are the times with the highest traffic of sales by Country:")
            highestTrafficCountry()
            print("Would you like to make another selection?")
            print('\t1. View Consumer Data gathered within the last two years')
            print('\t2. View top selling caregories of products')
            print('\t3. View top selling categories of products per Country')
            print('\t4. View how the popularity of products changes throughout the year')
            print('\t5. View how the popularity of products changes through the year by country')
            print('\t6. View which locations have the highest sales')
            print('\t7. View What times have the highest traffic of sales')
            print('\t9. Exit')
            sel = int(input("\nSelection: "))
        elif sel == 9:
            quit()
        else:
         print("Not a valid input")

          
startup()