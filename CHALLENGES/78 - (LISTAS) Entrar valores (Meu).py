#Esta forma esta incompleta, pois nao demonstra todas as posicoes onde aparece os maiores e menores... apenas a primeira...
lista = list()
for count in range(0, 5):
    lista.append(int(input('Digite o valor desejado ')))
print('-'*60)
print(f'O maior valor foi {max(lista)} e apareceu nas posicao {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)} e apareceu na posicao {lista.index(min(lista))}')
print('-'*60)
for c, c1 in enumerate(lista):
    print(f'termo {c} numero {c1}')


