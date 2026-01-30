#PROGRAM A EMPLOYEE PRORGAM TO RECEIVE INFORMATION LIKE: NAE, AGE, NIN, START OF CONTRACT, SALARY AND RETIREMENT YEAR.

from datetime import datetime
register = dict ()
register['Name'] = str(input('Name: '))
birth_year = int(input('Birth Year: '))
register['Age'] = datetime.now().year - birth_year
register['NIN'] = int(input('National Insurance (0 to disconsider) '))
if register['NIN'] !=0:
    register['Contract'] = int(input('Contract year: '))
    register['Salary'] = float(input('Salary: £'))
    register['Retirement'] = register['Age'] + ((register['Contract'] + 35) - datetime.now().year)

print('-'*60)
for k,v in register.items():
    print(f'The {k} is {v}')

print(register)
