lista_geral = list ()
pessoas = list ()
maior_peso = menor_peso = 0
print('-'*60)
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))

    if len(lista_geral) == 0:
        maior_peso = menor_peso = pessoas[1]
    if pessoas[1] > maior_peso:
        maior_peso = pessoas[1]

    if pessoas[1] < menor_peso:
        menor_peso = pessoas[1]

    lista_geral.append(pessoas[:])
    pessoas.clear()
    r = str(input('Voce quer continuar? S/N'))
    if r in 'Nn':
        break
    elif r in 'Ss':
        print('-'*60)
    else:
        r = str(input('Invalido!\nVoce quer continuar? S/N'))
print('-'*60)
print(f'O numero de pessoas cadastradas e de {len(lista_geral)}')

print(f'Com o maior peso {maior_peso} temos', end = ' ')

for c in range(0,len(lista_geral)):
    if lista_geral[c][1] == maior_peso:
        print(f'{lista_geral[c][0]}', end = ' ')

print(f'\nCom o menor peso {menor_peso} temos', end = ' ')

for b in range(0,len(lista_geral)):
    if lista_geral[b][1] == menor_peso:
        print(f'{lista_geral[b][0]}', end = ' ')




