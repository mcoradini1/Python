lista = list ()
while True:
    lista.append(int(input('Digite um numero ')))
    r = str(input('Quer continuar? S/N'))
    if r in 'Nn':
        break
lista.sort(reverse = True)
print(' - '*60)
print(f'[{len(lista)}] Numeros digitados\n Os valores em LISTA SAO: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('Nao foi encontrado o valor 5 na lista')

