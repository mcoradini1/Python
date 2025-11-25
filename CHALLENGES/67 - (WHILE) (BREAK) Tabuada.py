#quando digitar um numero negativo parar
n = 1
while n > 0:
    print('-' * 60)
    n = int(input('Digite a Tabuada que voce deseja '))
    print('-' * 60)
    n1 = 1
    while n > 0:
        print('{} * {} = {}'.format(n,n1,n1*n))
        n1 = n1 + 1
        if n1 == 11:
            break
print('Valor nao acessível, tente mais tarde')
