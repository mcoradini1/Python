#PROGRAM A DIE GAME, AND SET THE RESULTS IN ORDER OF THE HIGHEST VALUE:

from operator import itemgetter
from random import randint
from time import sleep

play_numbers = {'Marlon': randint(1, 6),
        'Su': randint(1,6),
        'Maria': randint(1,6),
        'Emmeline': randint(1,6)
                }

print('--- Rolling the Dice ---')
for j, k in play_numbers.items():
    print(f'{j} ROLL {k} on the dice!!\n')
    sleep(0.5)

#THE FUNCTION itemgetter() make a List with tuples inside, it's advisable to create another dictionary to do it,
#even setting it as a dictionary in the end it will become a list. I don't need to declare dictionary here, just made it
#to leave a comment.
ranking = dict ()


ranking = sorted(play_numbers.items(), key = itemgetter(1), reverse=True)
#RANKING WILL TAKE THE play_number.items and SORT it (By default it would sort by the term 0 (name), FOR THAT
#itemgetter(1) make it consider the term 1 (value), and then reverse, to organize from high to low.

print('-'*60)
print('\n')
for c,v in enumerate(ranking):
    print(f'In position {c+1} we have {v[0]} with score of {v[1]}')
    print('-'*60)
    sleep(0.5)

print(ranking)