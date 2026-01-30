#PROGARM TO PREPARE A SORTING GAME(LIKE MEGA-SENNA) ,THAT WILL PROVIDE 6 NUMBERS (CANNOT REPEAT WITHIN EACH PLAY)
#CHOOSE HOW MANY PLAYS, AND EACH PLAY WILL HAVE NUMBERS FROM 1 TO 60.

from random import randint
from time import sleep

list_general = list()
sort = [[0], [0], [0], [0], [0], [0]]
sorted_number = 0

t = int(input('How many sorts would you like? '))
print(f'{'-'*20}SORTING FOR YOU!! {'-'*20}\n')
for n in range (0,t):
    for b in range (0,6):
        sorted_number = randint(1, 60)
        while sorted_number in sort:
            sorted_number = randint(1, 60)
        sort[b] = sorted_number
    sort.sort()
    list_general.append(sort[:])


for e in range (0, t):
    print(f'PLAY NUMBER {e+1} -> {list_general[e]}')
    sleep(0.5)




