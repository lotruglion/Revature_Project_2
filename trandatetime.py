from random import randrange
import datetime
import pandas as pd


date_col = []
time_col = []


def change_time_format(a):

    if a < 10:

        return "0" + str(a)

    else:

        return str(a)


for i in range(1, 1000):
    random_minutes = change_time_format(randrange(59))
    random_hours = change_time_format(randrange(23))
    random_months = change_time_format(randrange(1, 8))
    if random_months == 2:
        random_days = change_time_format(randrange(1, 28))
    elif random_months in [1, 3, 5, 7, 8, 10, 12]:
        random_days = change_time_format(randrange(1, 30))
    else:
        random_days = change_time_format(randrange(1, 29))

    dt_str = random_days + "/" + random_months + "/2022" + \
        random_hours + ":" + random_minutes + ":00"

    date = datetime.datetime.strptime(dt_str, "%d/%m/%Y%H:%M:%S")
    date_col.append(date.date())
    time_col.append(date.time())

    d = {"datetime": date_col, "Time": time_col}

    df = pd.DataFrame(d)

    df.to_excel("output.xlsx", index=False)

    # df.to_excel("output.xlsx", index=False)
