# ====================================================================================================================
# CHALLENGE 39: Check Army Status: Considering that a person needs to enlist with 18 years old
# ====================================================================================================================

"""
Challenge: 4.11 - Check Army Status (039)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - import datetime
    - date.today().year
    - int()
    - if()
    - elif()
    - else()
    - print()

Tags: import datetime, date.today().year, int(), if(), elif(), else(), print()
Status: ✔️ Completed
"""

from datetime import date
today = date.today().year
birthday_year = int(input('Enter the year that your birthday year: '))
age = today - birthday_year

if age == 18:
    print('Your status is in ENLISTMENT YEAR ')
elif age < 18:
    print('Your status is NOT IN ENLISTMENT YEAR ')
else:
    print('Your ENLISTMENT YEAR was {} year ago'.format(age - 18))