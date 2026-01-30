#CREATE A PROGRAM TO SIMULATE AN ATM, IT WILL SHOW HOW MANY OF EACH BILL WILL BE USED
#CONSIDER BILLS OF: 1, 10, 20, 50
from math import trunc
continue_answer = 'Y'

while not continue_answer == 'N':

   #bill_50: int = 0
    #bill_20: int = 0
    #bill_10: int = 0
    #bill_1: int = 0
    #rest: int = 0

    print('-'*60)
    withdraw = int(input('How much do you want to withdraw? '))

    bill_50 = trunc(withdraw / 50)
    rest = withdraw % 50
    bill_20 = trunc(rest / 20)
    rest = rest % 20
    bill_10 = trunc(rest / 10)
    rest = rest % 10
    bill_1 = rest

    print(f'[BILLS 50] {bill_50}\n[BILLS 20] {bill_20}\n[BILLS 10] {bill_10}\n[BILLS 1] {bill_1}')
    print('-'*60)

    continue_answer = input(str('Would you like to continue Y/N? ')).upper().strip()

print('THANK YOU FOR USE OUR SERVICES! ')

