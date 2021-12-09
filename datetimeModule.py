"""
Attributes for datetime are: Year | Months | Days | Hours | Minutes | Seconds | Micro-seconds
We can perform arithmatic operations as well on time
"""
import datetime

print(datetime.date.today())

now = datetime.datetime.today()
old = datetime.datetime(1993,4,13,23,55)

age = now - old
print(now)
print(old)
print(age)