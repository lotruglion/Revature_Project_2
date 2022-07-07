import math
import os 
import pandas as pd
import random
import datetime
import csv

## site and weights
commerce = {
    'www.amazon.com' : 44,
    'www.eatfresh.com' : 17,
    'www.eathumanflesh.com' : 2,
    'www.gogofoods.com' : 12,
    'www.gainzfood.com' : 13,
    'www.notsafefoodforyou.com' : 10

} 
 ## the site names are for practice sake not for final product

##We have order_id, customer_id, customer_name, product_id, product_name, product_category, qty, price, country, city, 
## Do the datetime, and ecommerce_website_name  
##columns = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_success', 'faliure_reason']
ecommerce=['ecommerce_website_name']
df = pd.DataFrame(columns = ecommerce)
##save for just in case .keys()
#list must be made outside of loop when in a loop it become out of scope after loop is done

#list of keys to traverse through
randomlist=list(commerce.keys())
for i in range(100):
    #rand int to make the website random mod 6 so it does not go out of index
    rando=(i+random.randint(0,100))%6
    currentsite=randomlist[rando]    
    #we have to make sure the website has not be used completely
    while currentsite==0:
        rando=(i+random.randint(0,100))%6
        currentsite=randomlist[rando]    
    ecommerce.append(currentsite)
    commerce[currentsite]=commerce[currentsite]-1
print(ecommerce)
    
    # ##list comprehension
    # listcommerce = [ecommerce for ecommerce in commerce.keys()]
    # print(str(listcommerce))
    # ##defining weights
    # weights = [commerce[ecommerce][0]for ecommerce in commerce]
    # ecommerce = random.choices(listcommerce, weights = weights)[0]
    # ##ecommerce = random.choice(list(commerce, weights = weights))[0]
    # price = commerce[ecommerce]
    # df.loc[i] = [i, ecommerce, 1]

# df.to_csv('test_data.cvs')

# path = "eccommerce mail"
# files = [file for file in os.listdir(path) if not file.startswitch('.')]

# data1 = pd.DataFrame()

# for file in files:
#     current_data = pd.read_csv(path+"/"+file)
#     data1 = pd.concat([data1, current_data])

# data1.to_csv("all_data_copy.csv", index = False)

# all_data = pd.read_csv("all_data.csv")
# all.data.head(25)