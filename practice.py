from faker import Faker
import csv
from objects.customer import customer
from objects.payment import payment
from objects.product import product
import pandas as pd
from faker.providers import address
try:
    createfile=open('name.csv','x')
    createfile.close
except FileExistsError:
    print('File already exist overwriting')
filename="name.csv"
fakedata = Faker()



customer_names=[fakedata.unique.name() for i in range(500)] 
customer_country=[fakedata.current_country_code() for i in range(500)]
customer_city = [fakedata.city() for i in range(500)]

product_name= []
product_category=[]
product_price=[] 
with open("food.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      product_name.append(lines[0])
      product_category.append('food')
      product_price.append(fakedata.randomize_nb_elements(number= 20,le=True, max= 20) )
with open("movies.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      product_name.append(lines[0])
      product_category.append('movies')
      product_price.append(fakedata.randomize_nb_elements(number= 20) )
with open("cars.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      product_name.append(lines[0])
      product_category.append('cars')
      product_price.append(fakedata.randomize_nb_elements(number=10000) )

productWEB = {
    'www.amazon.com' : 44,
    'www.eatfresh.com' : 17,
    'www.eathumanflesh.com' : 2,
    'www.gogofoods.com' : 12,
    'www.gainzfood.com' : 13,
    'www.notsafefoodforyou.com' : 10

} 





#product_price = [fakedata.randomize_nb_elements(number= 100,le=True, max= 100) for i in range(2000)]

# for i in range(len(product_category)):
#     print("category: "+product_category[i]+" product: "+product_name[i])

# namelist=[]
customers={}
# payments={}
products={}
# orders= {}

for i in range(1,501):
      customers[i]=customer(i,customer_names[i-1],customer_country[i-1],customer_city[i-1])

for i in range(1,2001):
      products[i]=product(i,product_name[i-1], product_price[i-1],product_category[i-1],)

# for i in range(1,10001):
#     namelist.append(str(i)+','+str(i+3)+fakedata.name()+','+str(i+5))
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE)
#     namewriter.writerows([namelist])


