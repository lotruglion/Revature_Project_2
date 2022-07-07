#from pyspark.sql import SparkSession

from pydoc import doc
from tkinter import N, Y
from faker import Faker

import csv
import random

# header = ['order_id', 'customer_id', 'customer_name', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_txn_success', 'failure_reason']

# data = ['1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',]

# f = open('project_2_data', 'w')

# writer = csv.writer(f)

# writer.writerow(header)
# writer.writerow(data)

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


accepted = Y
declined = N

declinedTransaction = ["Card was declined", "Order Cancelled", "Out of Stock", "Card was declined", "Order Cancelled", "Out of Stock"]

do :

while True:
    print(random.choice(declinedTransaction))
    break
else:
    print("")