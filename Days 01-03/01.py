# Playing with datetime and timedelta
# This code needs refactorization


from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()

complete_today = datetime.today()

sleep_time = timedelta(hours=8)

# What is the date of the next Valentine's day

if today.month >= 2 and today.day >= 14:
    next_year = today.year + 1
    valentines_day = date(year=next_year, month=2, day=14)
else:
    valentines_day = date(year=today.year, month=2, day=14)

time_until_valentines_day = valentines_day - today

print("There are {} days left until Valentine's day".format(str(time_until_valentines_day.days)))

print(type(time_until_valentines_day))
print(time_until_valentines_day)

# What is the date of the next New Year's day

if today.month >= 1 and today.day >= 1:
    next_year = today.year + 1
    new_year_day = date(year=next_year, month=1, day=1)
else:
    new_year_day = date(year=today.year, month=1, day=1)

time_until_new_year_day = new_year_day - today

print("There are {} days left until New Year day".format(str(time_until_new_year_day.days)))
