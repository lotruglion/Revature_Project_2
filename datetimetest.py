from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import unix_timestamp, from_unixtime

spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("backup.csv", inferSchema=True, header=True)

# df.show()

# df.withColumn("todays_date", F.current_date()).show()

# df.withColumn("todays_date_time", F.current_timestamp()).show()
# df.printSchema()
df2 = df.select("datetime", from_unixtime(
    unix_timestamp("datetime", "yyyy-MM-dd HH:MM:ss")).alias("new_date"))
df2.show()

(df2.withColumn("to_date", F.to_date("datetime")).withColumn(
    "to_date", F.to_date("datetime")).show())
