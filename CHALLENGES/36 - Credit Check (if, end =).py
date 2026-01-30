#PROGRAM A SIMPLE CREDIT CHECK, CONSIDERING
#THE MONTHLY VALUE CANNOT BE HIGHER THAN 30% OF THE PERSON MONTHLY WAGE.


house = float(input('What is the price of the house: '))
salary = float(input('What is the family salary: '))
finance_time_year = int(input('How long will be divide: '))
installments = house / (finance_time_year * 12)
if installments > 0.3 * salary:
    print('DENIED, The month installment will be ({:.2f}£) , higher than 30% of your family salary ({:.2f} £)'.format(installments, salary * 0.3))
else:
    print('APPROVED, The month installment will be ({:.2f}£), lower than 30% of your family salary ({:.2f} R$)'.format(installments, salary * 0.3))
    print('SYSTEM CLOSE', end='-'*8)
