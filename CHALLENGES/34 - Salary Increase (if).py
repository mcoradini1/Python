#PROGRAM TO INCREASE SALARIES WITH THE RULE ABOVE:
#ABOVE 1250,00 £ (+10%), BELLOW (+15%)

salary = float(input('What is your salary: ? '))
if salary > 1250:
    print('The new salary is {} \nA 10% increase '.format(salary + (salary * 0.1)))
    print('{:.2f} * 10% = {:.2f}'.format(salary, salary * 0.10))
else:
    print('{:.2f} * 15% = {:.2f}'.format(salary, salary * 0.15))
    print('The new salary is {} \nA 15% increase'.format(salary + (salary * 0.15)))