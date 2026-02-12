#PROGRAM TO THINK A NUMBER BETWEEN 0 AND 5
import time
import random

computer = random.randint(0, 5)
print(computer)
print('-==-' * 20)
print('I am thinking of a number between 0 and 5' )
print('-==-' * 20)
player = int(input('Which number would you like to guess? '))
print('PROCESSING...')
time.sleep(2)
if player == computer:
    print('Congratulations! My number is {}!'.format(computer))
else:
    print('WRONG NUMBER! I thought about {}'.format(computer))