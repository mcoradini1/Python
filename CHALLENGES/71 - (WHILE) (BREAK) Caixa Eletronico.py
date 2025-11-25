from math import trunc
continuar = 'S'

while not continuar == 'N':

    nota50 = 0
    nota20 = 0
    nota10 = 0
    nota1 = 0
    resto = 0
    print('-'*60)
    saque = int(input('Quanto gostarias de sacar? '))

    nota50 = trunc(saque/50)
    resto = saque%50
    nota20 = trunc(resto/20)
    resto = resto%20
    nota10 = trunc(resto/10)
    resto = resto%10
    nota1 = resto

    print(f'[Notas 50] {nota50}\n[Notas 20] {nota20}\n[Notas 10] {nota10}\n[Notas 1] {nota1}')
    print('-'*60)

    continuar = input(str('Voce gostaria de continuar S/N? ')).upper().strip()

print('Obrigado por usar este servico')

