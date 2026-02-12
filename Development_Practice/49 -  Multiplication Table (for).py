#CREATE A MULTIPLICATION TABLE USING FOR
n = int(input('Type the multiplication table that you need: '))
for c in range (1,11):
    print('{} * {} = {}'.format(c,n,c*n))