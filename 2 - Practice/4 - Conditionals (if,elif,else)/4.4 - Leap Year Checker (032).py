# ==============================================================================================================
# CHALLENGE 32: Leap Year Checker: List of leap year (2024, 2028)
# ==============================================================================================================

"""
Challenge: 4.4 - Leap Year Checker (032)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - import datetime
    - date.today()
    - int()
    - if()
    - else()
    - .format
    - print()


Tags: import datetime, date.today(), float(), if(), else(), .format, print()
Status: ✔️ Completed
"""

from datetime import date
year = int(input('Type the year '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a LEAP YEAR'.format(year))
else:
    print('{} is NOT a LEAP YEAR'.format(year))