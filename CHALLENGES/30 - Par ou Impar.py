# Ler um numero e decidir se e par ou impar
numero = int(input('Entre um numero '))
check = numero%2
if(check==0):
    print('O numero {} e par'.format(numero))
else:
    print('O numero {} e impar'.format(numero))