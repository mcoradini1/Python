lista = list()
while True:
    n = int(input('Digite um valor '))
    if n not in lista:
        lista.append(n)
        print('--- O valor foi adicionado com SUCESSO! ---')
    else:
        print(' --- Valor duplicado, Nao foi adicionado --- ')
    r = str(input('Voce quer continuar? S/N '))
    if r in 'Nn':
        break
print('-'*60)
lista.sort()
print(f'Voce digitou os valores {lista}')


