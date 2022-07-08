from faker import Faker
import csv
from objects.customer import customer
from objects.payment import payment
from objects.product import product
import pandas as pd
try:
    createfile=open('name.csv','x')
    createfile.close
except FileExistsError:
    print('File already exist overwriting')
filename="name.csv"
fakedata = Faker()
productname= []
pandas_data = pd.read_csv('food.csv',sep='|',usecols = ["productname"])
print(pandas_data)
# names=[fakedata.unique.name() for i in range(500)] 


# namelist=[]
# customers={}
# payments={}
# products={}
# #using dictionary to randomise where the customerid is the key and the value is the name
# for i in range(1,501):
#     customers[i]=customer(i,names[i-1])
#     print(str(customers[i]))
# # for i in range(1,2001):
# #      products[i]=product(i,productname[i-1])

# for i in range(1,10001):
#     namelist.append(str(i)+','+str(i+3)+fakedata.name()+','+str(i+5))
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE)
#     namewriter.writerows([namelist])


