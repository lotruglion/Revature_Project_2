# project 2
import pandas as pd
import numpy
import random
import csv


payment = [['Card'],
           ['Card'],
           ['Card'],
           ['Card'],
           ['Wallet'],
           ['Wallet'],
           ['Wallet'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['Internet Banking'],
           ['UPI'],
           ['UPI']]

header = ['payment_type']

payment_type = {}
data = [payment]

# columns = ['payment_type']

# df = pd.DataFrame(columns=columns)
f = open('test_paymentdata.csv', 'a')

writer = csv.writer(f)

writer.writerow(header)

for payment_type in range(1, 10000):
    writer.writerow(random.choice(payment))

f.close()

# print('Current iteration: '+str(i)+' cur
