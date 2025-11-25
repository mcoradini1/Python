contador = 0
n = int(input('Digite um numero '))
for c in range (1, n+1):
    if(n%c == 0):
        print('\033[33m{}'.format(c), end = ' ')
        contador+= 1
    else:
        print('\033[m{}'.format(c), end  = ' ')
    #print(c, end=' ')
if(contador == 2):
    print('\n\n\033[mO numero e primo, ele apenas e divisivel por \033[33m{} \033[mnumeros'.format(contador))
else:
    print('\n\n\033[mO numero nao e primo,ele e divisivel por \033[33m{} \033[mnumeros'.format(contador))




