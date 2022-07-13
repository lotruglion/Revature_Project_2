from faker import Faker 
from faker.providers import date_time

test1 = Faker()

for i in range(2):
  print(test1.date(pattern: str = '%2021-%01-%01', end_datetime: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None] = None)))