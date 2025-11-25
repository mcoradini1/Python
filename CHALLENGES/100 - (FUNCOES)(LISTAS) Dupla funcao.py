from random import randint
from time import sleep
numeros = list()


def sorteia():
    for c in range (0,5):
        numeros.append(randint(0,999))
    print('Sorteados')
    for b in numeros:
        print(f'{b} ', end=' ')
        sleep(0.3)

def somaPar():
    soma1 = 0
    for bb in numeros:
        if bb%2 == 0:
            soma1 += bb
    print(f'\nSomatorio dos pares e {soma1}')

sorteia()
somaPar()