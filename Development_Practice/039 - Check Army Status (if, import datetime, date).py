#PROGRAM TO CHECK THE ARMY STATUS

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