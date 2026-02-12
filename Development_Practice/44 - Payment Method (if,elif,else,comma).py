#A PROGRAM TO GET A USE A PAYMENT METHOD TO DISCOUNT/DIVIDE THE BILL IN INSTALMENTS

bill_price = float(input('Type the bill price: '))
print('''The types of payment are:

[1] On cash (10% discount)
[2] Debit Card (5% discount)
[3] Credit card divided in 2x (Same price)
[4] Credit card divided in 3x ou mais (extra 20%)
''')
way_payment = int(input('Which type of payment do you want? '))

if way_payment == 1:
    print('Your paid {:.2f}£ on cash '.format(bill_price * 0.9))
elif way_payment == 2:
    print('You paid {:.2f}£ on debit card'.format(bill_price * 0.95))
elif way_payment == 3:
    print('You divided {:.2f}£, in 2 installments of {:.2f}'.format(bill_price, bill_price / 2))
elif way_payment ==4:
    installments = int(input('How many times do you want to divide? '))
    print('Your last bill will be {:.2f}£, in {} installments of {:.2f}£'.format(bill_price * 1.2, installments, bill_price * 1.2 / installments))

