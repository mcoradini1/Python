#numeros de 1 a 60 e nao podem repetir...
from random import randint
from time import sleep
lista = list()
sorteio = [[0],[0],[0],[0],[0],[0]]
sorteado = 0

t = int(input('Quantos jogos voces querem os palpites '))
print(f'{'-'*20}SORTEANDO PARA VOCE {'-'*20}\n')
for n in range (0,t):
    for b in range (0,6):
        sorteado = randint(1, 60)
        while sorteado in sorteio:
            sorteado = randint(1,60)
        sorteio[b] = sorteado
    sorteio.sort()
    lista.append(sorteio[:])


for e in range (0, t):
    print(f'JOGO NUMERO {e+1} -> {lista[e]}')
    sleep(0.5)




