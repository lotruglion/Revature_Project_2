##project 2
import os 
import pandas as pd
import random
import datetime

commerce = {
    'www.amazon.com' : 1,
    'www.eatfresh.com' : 5
    
} 
 
##We have order_id, customer_id, customer_name, product_id, product_name, product_category, qty, price, country, city, 
## Do the datetime, and ecommerce_website_name  
##columns = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_success', 'faliure_reason']
columns = ['ecommerce_website_name']

df = pd.DataFrame(columns = columns)
##.keys()
for i in range(10):
    listcommerce = [ecommerce for ecommerce in commerce]
    weights = [commerce[ecommerce][0]for commerce in ecommerce]
    ecommerce = random.choices(listcommerce, weights = weights)[0]
    price = commerce[ecommerce]
    df.loc[i] = [i, ecommerce, 1]

print(ecommerce)
print(weights)
"""
df.to_csv('test_data.cvs')

path = "*have a file name*"
files = [file for file in os.listdir(path) if not file.startswitch('.')]

data1 = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    data1 = pd.concat([data1, current_data])

data1.to_csv("all_data_copy.csv", index = False)

all_data = pd.read_csv("all_data.csv")
all.data.head(25)
"""