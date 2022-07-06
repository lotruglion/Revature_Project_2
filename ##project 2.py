##project 2

from itertools import product
import os 
import pandas as pd
import numby
import random
import datetime

products = {
    'Bread': 2.79,
    'Eggs': 4.00,
    'Rice': 1.70,
    'Butter': 2.92,
    'Milk': 2.99
} 
def generate_random_address():
    street_name = ['Main']
    cities = ['Colorado']
    country = ['America FY']

product_list =     
columns = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_success', 'faliure_reason']
order_id = 1
customer_id = 1
##product_id = 1
df = pd.DataFrame(columns = columns)

for i in range(order_amount):
    product = random.choices(products.keys())[0]
    price = products[product]
    df.loc[i] = [i, product, 1, price, ]

    order_id += 1
    customer_id += 1
    ##prodcut_id = 
"""
df.to_csv('test_data.cvs')

path = "*have a file name*"
files = [file for file in os.listdir(path) if not file.startswitch('.')]

all_month_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    all_months_data = pd.concat([all_months_data, current_data])

all_months_data.to_csv("all_data_copy.csv", index = False)

all_data = pd.read_csv("all_data.csv")
all.data.head(25)
"""