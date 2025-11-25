from operator import itemgetter
from random import randint
from time import sleep

jogo = {'Marlon': randint(1,6),
        'Su': randint(1,6),
        'Maria': randint(1,6),
        'Emmeline': randint(1,6)
}

print('--- Valores sorteados ---')
for j, k in jogo.items():
    print(f'O {j} sorteou {k} no dado.')
    sleep(0.5)

ranking = dict ()   #a funcao itemgather faz lista com tuplas dentro...
                    #aconselhado a criar outro dicionario para fazer isto
                    #mesmo determinando ese como dicionario, no final ele se tornou uma lista...
                    #poderia ter deixado como apenas lista aqui...


ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
    #ranking vai ter um sorted de JOGO.ITEMS... e eu vou ordenar pelo valor na posicao 1 (no caso o valor)
    #por isso no itemgather tenho 1
print('-'*60)
print('\n')
for c,v in enumerate(ranking):
    print(f'Na posicao {c+1} temos {v[0]} com {v[1]}')
    print('-'*60)
    sleep(0.5)
