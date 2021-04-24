# Write a program to get next day of a given date

from datetime import date, timedelta
import calendar

year=int(input("Year:"))
month=int(input("\nMonth:"))
day=int(input("\nDay:"))

try:
    date = date(year, month, day)
except:
    print("\nPlease Enter a Valid Date\n")

date += timedelta(days=1)

print(date)