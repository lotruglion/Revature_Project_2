from faker import Faker
import csv
import random
import string
from objects.customer import customer
from objects.order import order
from objects.completeOrder import completeOrder
from objects.payment import payment
from objects.product import product
import pandas as pd
from faker.providers import address
import time


def readFile(fileName):
    rowsList = []
    try:
        with open(fileName, 'r') as f:
            file = csv.reader(f)
            rowsList=list(file)
    except FileNotFoundError:
        print('File does not exist')
    return rowsList

def appendToCsv(fileName,row):
    try:
        with open(fileName, 'a+',newline="") as f:
            write = csv.writer(f)
            write.writerow(row)

    except FileNotFoundError:
        print('File does not exist')

def extractCustomers(mappedObjects,rows):
    for row in rows:
        if row[1] not in (mappedObjects[1]):
            (mappedObjects[1])[row[1]] = customer(row[1],row[2],row[10],row[11])
    # for key in mappedObjects[1]:
    #     print((mappedObjects[1])[key])

def extractPayment(mappedObjects,rows):
    for row in rows:
        if row[13] not in (mappedObjects[2]):
            (mappedObjects[2])[row[13]] = payment(row[13],row[7],row[14],row[15])
    # for key in mappedObjects[2]:
    #     print((mappedObjects[2])[key])

def extractProduct(mappedObjects,rows):
    for row in rows:
        if row[3] not in (mappedObjects[3]):
            (mappedObjects[3])[row[3]] = product(row[3],row[4],row[8],row[5],row[12])
    # for key in mappedObjects[3]:
    #     print((mappedObjects[3])[key])

def extractOrder(mappedObjects,rows,products):
    #count = 0
    for row in rows:
        #print(row[0])
        if row[0] in (mappedObjects[0]):
            currentOrder=(mappedObjects[0])[row[0]]
            # print(row[0])
            # print(currentOrder.orderID)
            if products[row[3]] not in currentOrder.products and currentOrder.orderID==row[0]:
                (mappedObjects[0])[row[0]].addProduct(products[row[3]])
        else:
            (mappedObjects[0])[row[0]] = completeOrder(row[0],row[6],row[9],products[row[3]])   
        # +=1
    print(len((mappedObjects[0])['13922'].products))
        # print('Count: '+str(count)) 
    # for key in mappedObjects[0]:
    #     print(len((mappedObjects[0])[key].products))

def extractOrderSimple(mappedObjects,rows):
    for row in rows:
        #print(row[0])
        if row[0] not in (mappedObjects[0]):
            currentOrder=(mappedObjects[0])[row[0]]=order(row[0],row[9])
    # for key in mappedObjects[0]:
    #     print((mappedObjects[0])[key])
        

def processAndSort(rows):
    orders = {}
    customers = {}
    transactions = {}
    products={}
    mappedObjects = [orders,customers,transactions,products]
    extractCustomers(mappedObjects,rows)
    extractPayment(mappedObjects,rows)
    extractProduct(mappedObjects,rows)
    #extractOrder(mappedObjects,rows,mappedObjects[3])
    extractOrderSimple(mappedObjects,rows)
    return mappedObjects

def randomGen(orders,customers,transactions,products):
    orderID=str(random.randint(10000,10000000))
    while orderID in orders:
        orderID=str(random.randint(10000,10000000))
    randomCustomer=random.choice(list(customers.values()))
    transactionID='INTGFD23DB3'
    while transactionID in transactions or transactionID=='INTGFD23DB3':
        transactionID='INTGFD23DB3'
        tid=random.randint(1,10000000)
        tLetter=random.choice(string.ascii_letters)
        transactionID=transactionID+tLetter+str(tid)
    randomPayment=random.choice(list(transactions.values()))
    randomProduct=random.choice(list(products.values()))
    qty=str(random.randint(1,123))
    date=random_date("1/1/2020 1:10 PM", "1/1/2023 1:10 AM", random.random())
    return [orderID,randomCustomer.customerID,randomCustomer.customerNAME,randomProduct.productID,randomProduct.productNAME,randomProduct.productCATEGORY,qty,randomPayment.paymentTYPE,randomProduct.price,date,randomCustomer.customerCOUNTRY,randomCustomer.customerCITY,randomProduct.productWEB,tid,randomPayment.paymentSUCCESS,randomPayment.paymentFAILreason]

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def randomAdd(fileName):
    rows=readFile(fileName)
    sorted=processAndSort(rows)
    randomRow=randomGen(sorted[0],sorted[1],sorted[2],sorted[3])
    appendToCsv(fileName,randomRow)
    print("Row added"+str(randomRow))

for i in range(0,100):
    fileName='backup.csv'
    randomAdd(fileName)
    time_duration=10
    time.sleep(time_duration)
# for row in rows:
#     for column in row:
#         print(column+' type:')
#         print(type(column))

#test = ['121465564564', '1456461', "TEST", '576', "TEST", 'Test', '25','Test', '324343', '11/12/2021 22:01', 'TEST', '23432432', 'test.com', 'INTGFD23wef43345952', 'Y', '']
#appendToCsv('backup.csv',test)











# try:
#     createfile=open('name.csv','x')
#     createfile.close
# except FileExistsError:
#     print('File already exist overwriting')
# filename="name.csv"
# fakedata = Faker()



# customer_names=[fakedata.unique.name() for i in range(500)] 
# customer_country=[fakedata.current_country_code() for i in range(500)]
# customer_city = [fakedata.city() for i in range(500)]

# product_name= []
# product_category=[]
# product_price=[] 
# with open("food.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('food')
#       product_price.append(fakedata.randomize_nb_elements(number= 20,le=True, max= 20) )
# with open("movies.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('movies')
#       product_price.append(fakedata.randomize_nb_elements(number= 20) )
# with open("cars.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('cars')
#       product_price.append(fakedata.randomize_nb_elements(number=10000) )

# productWEB = {
#     'www.amazon.com' : 44,
#     'www.eatfresh.com' : 17,
#     'www.eathumanflesh.com' : 2,
#     'www.gogofoods.com' : 12,
#     'www.gainzfood.com' : 13,
#     'www.notsafefoodforyou.com' : 10

# } 


#order_quntity= [fakedata.randomize_nb_elements(number= 10,le=True, max= 20) )]
#order_date=[]


#product_price = [fakedata.randomize_nb_elements(number= 100,le=True, max= 100) for i in range(2000)]

# for i in range(len(product_category)):
#     print("category: "+product_category[i]+" product: "+product_name[i])

# namelist=[]
#customers={}
# payments={}
# products={}
# orders= {}

# for i in range(1,501):
#       customers[i]=customer(i,customer_names[i-1],customer_country[i-1],customer_city[i-1])

# for i in range(1,2001):
#       products[i]=product(i,product_name[i-1], product_price[i-1],product_category[i-1],)
# for i in range(1,10001):
#       orders[i]=order(1,)

# for i in range(1,10001):
#     namelist.append(str(i)+','+str(i+3)+fakedata.name()+','+str(i+5))
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE)
#     namewriter.writerows([namelist])












# try:
#     createfile=open('name.csv','x')
#     createfile.close
# except FileExistsError:
#     print('File already exist overwriting')
# filename="name.csv"
# fakedata = Faker()



# customer_names=[fakedata.unique.name() for i in range(500)] 
# customer_country=[fakedata.current_country_code() for i in range(500)]
# customer_city = [fakedata.city() for i in range(500)]

# product_name= []
# product_category=[]
# product_price=[] 
# with open("food.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('food')
#       product_price.append(fakedata.randomize_nb_elements(number= 20,le=True, max= 20) )
# with open("movies.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('movies')
#       product_price.append(fakedata.randomize_nb_elements(number= 20) )
# with open("cars.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#       product_name.append(lines[0])
#       product_category.append('cars')
#       product_price.append(fakedata.randomize_nb_elements(number=10000) )

# productWEB = {
#     'www.amazon.com' : 44,
#     'www.eatfresh.com' : 17,
#     'www.eathumanflesh.com' : 2,
#     'www.gogofoods.com' : 12,
#     'www.gainzfood.com' : 13,
#     'www.notsafefoodforyou.com' : 10

# } 


#order_quntity= [fakedata.randomize_nb_elements(number= 10,le=True, max= 20) )]
#order_date=[]


#product_price = [fakedata.randomize_nb_elements(number= 100,le=True, max= 100) for i in range(2000)]

# for i in range(len(product_category)):
#     print("category: "+product_category[i]+" product: "+product_name[i])

# namelist=[]
#customers={}
# payments={}
# products={}
# orders= {}

# for i in range(1,501):
#       customers[i]=customer(i,customer_names[i-1],customer_country[i-1],customer_city[i-1])

# for i in range(1,2001):
#       products[i]=product(i,product_name[i-1], product_price[i-1],product_category[i-1],)
# for i in range(1,10001):
#       orders[i]=order(1,)

# for i in range(1,10001):
#     namelist.append(str(i)+','+str(i+3)+fakedata.name()+','+str(i+5))
# with open(filename,'w',newline='') as csvfile:
#     namewriter=csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE)
#     namewriter.writerows([namelist])