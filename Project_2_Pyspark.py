from pyspark import SparkContext, sql, SparkConf
from pyspark.sql import SparkSession, Row, HiveContext, SQLContext
import pyspark
from pyspark.sql.functions import col
import os
import sys


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession\
    .builder\
    .appName("Project_2")\
    .master("local[*]")\
    .getOrCreate()

sc = spark.sparkContext
sqlcontext = SQLContext(spark)


df_pyspark=spark.read.csv('backup.csv')

df_pyspark.show()


















# Transactions = [["N, Card was declined"], ["N, Order Cancelled"], ["N, Out of Stock"], ["N, Card was declined"], ["N, Order Cancelled"], ["N, Out of Stock"], 
# ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"], ["Y"]]

# header = ["Transaction Success", "Reason for Failure"]

# data = [Transactions]

# f = open('project_2_data_Example', 'w')

# writer = csv.writer(f)

# writer.writerow(header)
# for transactions in range(10000):
#     writer.writerow(random.choice(Transactions))


# f.close()






# doclist=["Physician", "Specialist"]
# fake=Faker()
# mylist = ["Male", "Female", "Other"]
# i=1
# while i<51:
#names.get_full_name(), random.randrange(82)+18, mylist[random.randrange(3)]

#JiaYing's code
# try:
#     createfile=open('name.csv','x')
#     createfile.close
# except FileExistsError:
#     print('File already exist overwriting')
# filename="name.csv"
# fakedata = Faker()
# fakedata.name()
# namelist=[]
# for i in range(3):
#     namelist.append(fakedata.name())
#     print(namelist[i])
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',')
#     namewriter.writerows([namelist])