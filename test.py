from faker import Faker 

test1 = Faker()

for i in range(2):
  print(test1.price())