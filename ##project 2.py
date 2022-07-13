##project 2
import math
import os 
import pandas as pd
import random
import datetime
import csv

commerce = {
    'www.amazon.com' : 33,
    'www.eatfresh.com' : 17,
    'www.eathumanflesh.com' : 2,
    'www.gogofoods.com' : 12,
    'www.gainzfood.com' : 13,
    'www.notsafefoodforyou.com' : 10,
    'www.foodforall.com' : 26,
    'www.foodfoodfood.com' : 20,
    'www.foodforthought.com' : 22,
    'www.suprisefoodattack' : 15
} 
 ## the site names are for practice sake not for final product

##We have order_id, customer_id, customer_name, product_id, product_name, product_category, qty, price, country, city, 
## Do the datetime, and ecommerce_website_name  
##columns = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_success', 'faliure_reason']
columns = ['ecommerce_website_name']

df = pd.DataFrame(columns = columns)
##save for just in case .keys()
## MAYBE random range between 0-10 = amazon then do the same with the other sites 

#list must be made outside of loop when in a loop it become out of scope after loop is done
ecommerce=[]

#list of keys to traverse through
randomlist=list(commerce.keys())

mod=6

for i in range(100):
#rand int to make the website random mod 6 so it does not go out of index
    if len(randomlist)==0:
            break
    rando=(i+random.randint(0,100))%mod
    currentsite=randomlist[rando]
     #we have to make sure the website has not be used completely
    while commerce[currentsite]==0:
        print("Random value: "+str(rando)+" Currentsite: "+currentsite+" Currentsite weight left:"+str(commerce[currentsite]))
        mod= mod-1
        print("mod: "+str(mod))
        randomlist.remove(currentsite)
        if len(randomlist)==0:
            break
        rando=0 if mod==0 else (i+random.randint(0,100))%mod
        currentsite=randomlist[rando]
    ecommerce.append(currentsite)
    commerce[currentsite]=commerce[currentsite]-1
print(ecommerce)


df.to_csv('test_data.cvs')

path = "eccommercemail"
files = [file for file in os.listdir(path) if not file.startswitch('.')]

data1 = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    data1 = pd.concat([data1, current_data])

data1.to_csv("all_data_copy.csv", index = False)

all_data = pd.read_csv("all_data.csv")
all.data.head(25)