# ==========================================================================================================
# CHALLENGE 28: Guess the number: Think a number between 0 and 5.
# ==========================================================================================================

"""
Challenge: 11.2 - Guess the number (28)
Category: 11 - Mini-Projects
Concepts Used:
    - import time
    - import random
    - randint()
    - sleep()
    - int()
    - .format
    - print()

Tags: time, random, randint(), sleep(), int(), .format(), print()
Status: ✔️ Completed
"""

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