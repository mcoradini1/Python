#Crie um programa que le um numero real na tela e mostre sua forma inteira
#import math
from math import trunc

r = float(input('Entre um numero: '))
print('seu numero e {}'.format(int(r)))

print('\n\nO seu numero e {} \ne sua porcao inteira e {}'.format(r, trunc(r)))

#print('\n\nO seu numero e {} \ne sua porcao inteira e {}'.format(r, math.trunc(r)))