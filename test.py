from faker import Faker 
from faker.providers import date_time

test1 = Faker()

for i in range(2):
  print(test1.date())