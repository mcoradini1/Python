#CHECK IF THE YEAR IS A LEAP YEAR
#FOR CHECK - 2024,2028 (LEAP YEAR) --- 2025, 2027 (NOT LEAP YEAR)
from datetime import date
year = int(input('Type the year '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a LEAP YEAR'.format(year))
else:
    print('{} is NOT a LEAP YEAR'.format(year))