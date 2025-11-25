import random
import time

#poderia por from random import... ou from time import

computador = random.randint(0,5)
print(computador)
print('-==-' * 20)
print('Vou pensar um numero entre 0 e 5. Tente adivinhar' )
print('-==-' * 20)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('Parabens voce me venceu!')
else:
    print('Voce perdeu seu banana, eu pensei no numero {}, e voce disse {}'.format(computador,jogador))