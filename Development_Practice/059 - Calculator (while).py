#PROGRAM A SIMPLE CALCULATOR THAT WILL RED TWO NUMBERS AND:
#SUM, MULTIPLY, HIGHER NUMBER, NEW NUMBERS, EXIT PROGRAM

n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
higher = 0
choice = 0

while  choice < 5:
    print('\n[1] SUM\n[2] MULTIPLY\n[3] HIGHER NUMBER\n[4] NEW NUMBERS\n[5] EXIT\n')
    choice = int(input('O que deseja efetuar? '))

    if choice == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    if choice == 2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    if choice == 3:
        if n1 > n2:
            higher=n1
        else:
            higher=n2
        print('The higher number is {}'.format(higher))
    if choice == 4:
        n1 = int(input('Type the first number: '))
        n2 = int(input('Type the second number: '))
    if choice >= 6:
        print('INVALID COMMAND')
        choice = 0

if choice == 5:
    print('PROGRAM CLOSED')

