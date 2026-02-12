from random import randint
from time import sleep
numbers_list = list()


def sort_funct():
    for c in range (0,5):
        numbers_list.append(randint(0, 999))
    print('Sorted')
    for b in numbers_list:
        print(f'{b} ', end=' ')
        sleep(0.3)

def sum_if_even():
    soma1 = 0
    for bb in numbers_list:
        if bb%2 == 0:
            soma1 += bb
    print(f'\nSum of evens {soma1}')

sort_funct()
sum_if_even()