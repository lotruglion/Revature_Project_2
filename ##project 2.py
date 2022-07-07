##project 2
import os 
import pandas as pd
import random
import datetime
import csv

commerce = {
    ## site and weights
    'www.amazon.com' : [24],
    'www.eatfresh.com' : [16],
    'www.eathumanflesh.com' : [1],
    'www.gogofoods.com' : [12],
    'www.gainzfood.com' : [3],
    'www.notsafefoodforyou' : [4]

} 
 ## the site names are for practice sake not for final product

##We have order_id, customer_id, customer_name, product_id, product_name, product_category, qty, price, country, city, 
## Do the datetime, and ecommerce_website_name  
##columns = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_success', 'faliure_reason']
columns = ['ecommerce_website_name']

df = pd.DataFrame(columns = columns)
##save for just in case .keys()
for i in range(10):
    ##list comprehension
    listcommerce = [ecommerce for ecommerce in commerce]
    ##defining weights
    weights = [commerce[ecommerce][0]for ecommerce in commerce]
    ecommerce = random.choices(listcommerce, weights = weights)[0]
    ##ecommerce = random.choice(list(commerce, weights = weights))[0]
    price = commerce[ecommerce]
    df.loc[i] = [i, ecommerce, 1]

df.to_csv('test_data.cvs')

path = "eccommerce mail"
files = [file for file in os.listdir(path) if not file.startswitch('.')]

data1 = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    data1 = pd.concat([data1, current_data])

data1.to_csv("all_data_copy.csv", index = False)

all_data = pd.read_csv("all_data.csv")
all.data.head(25)