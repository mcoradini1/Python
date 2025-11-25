#Falta remover os valores repetidos... colocando frase para repetir estes...
lista_completa = list()
lista_unica = list()
resposta = 'S'
while resposta == 'S':
    lista_completa.append(int(input('Entre um valor ')))
    if lista_completa[-1] not in lista_unica:
        lista_unica.append(lista_completa[-1])
    else:
        print('Ja obtemos este valor, vou desconsiderar')

    resposta = str(input('Voce quer continuar? S/N ')).upper()


    while resposta != 'S' and resposta != 'N':
        resposta = input('Resposta Invalida!\nVoce quer continuar? S/N ').upper().strip()

lista_unica.sort()
print(f'{lista_completa} e {lista_unica}')

for count in lista_unica:
    print(f'{count}', end = ' -> ')
    print('FIM')

