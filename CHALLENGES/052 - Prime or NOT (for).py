#PROGRAM TO CHECK IF A NUMBER IS PRIME, USE COLORS TO EDIT:

cont_prime = 0
n = int(input('Type a number '))
for c in range (1, n+1):
    if n%c == 0:
        print('\033[33m{}'.format(c), end = ' ')
        cont_prime+= 1
    else:
        print('\033[m{}'.format(c), end  = ' ')
    #print(c, end=' ')
if(cont_prime == 2):
    print('\n\n\033[mThe number is PRIME, It is divided by \033[33m{} \033[mnumbers'.format(cont_prime))
else:
    print('\n\n\033[mThe number is NOT PRIME,It is divided by \033[33m{} \033[mnumbers'.format(cont_prime))




