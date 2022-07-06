#from pyspark.sql import SparkSession

import csv

header = ['order_id', 'customer_id', 'customer_name', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_txn_success', 'failure_reason']

data = ['1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',]

f = open('project_2_data', 'w')

writer = csv.writer(f)

writer.writerow(header)
writer.writerow(data)

f.close()