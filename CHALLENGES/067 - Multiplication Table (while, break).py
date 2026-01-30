#PROGRAM TO CREATE A MULTIPLICATION TABLE THAT WILL CLOSE IN CASE OF NEGATIVE NUMBER
n = 1
while n > 0:
    print('-' * 60)
    n = int(input('Type the multiplication table of your choice: '))
    print('-' * 60)
    n1 = 1
    while n > 0:
        print('{} * {} = {}'.format(n,n1,n1*n))
        n1 = n1 + 1
        if n1 == 11:
            break
print('Inaccessible value! Shutting down!')
