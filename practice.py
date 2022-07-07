from faker import Faker
import csv
from objects.customer import customer
from objects.payment import payment
from objects.product import product
try:
    createfile=open('name.csv','x')
    createfile.close
except FileExistsError:
    print('File already exist overwriting')
filename="name.csv"
fakedata = Faker()
names=[fakedata.unique.name() for i in range(500)]
# namelist=[]
customers={}
payments={}
products={}

for i in range(1,501):
    customers[i]=customer(i,names[i-1])
    # print('Current iteration: '+str(i)+' current customer: '+str(customers[i]))

# for i in range(1,10001):
#     namelist.append(str(i)+','+str(i+3)+fakedata.name()+','+str(i+5))
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',')
#     namewriter.writerows([namelist])


