somatorio = 0
contador = 0
for c in range(1, 7):
    n = int(input('Digite um {} valor '.format(c)))
    if(n%2 == 0):
        somatorio = somatorio + n
    else:
        contador = contador + 1

print('\n\n{} Pares \n{} Impares \n{} Soma dos pares'.format(6-contador,contador,somatorio))