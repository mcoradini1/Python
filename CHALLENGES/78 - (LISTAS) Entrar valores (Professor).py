lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um numero para a posicao {c} ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print('-'*60)
print(f'O maior termo da lista e {maior} e o menor termo e {menor}\nA lista completa e {lista}')
print('-'*60)
