# ======================================================================================================================
# CHALLENGE 58: Guess Game: We will try to guess a number between 0 and 10, i will count in how many attempts we've done
# ======================================================================================================================

"""
Challenge: 5.2.2 - Guess Game (058)
Category: 5 - Loops
Concepts Used:
    - while
    - import random
    - randint()
    - if()



Tags: while, import random, randint(), if()
Status: ✔️ Completed
"""

import random
guess_try = 0
guess = -1
machine_guess = random.randint(0, 10)

while guess != machine_guess:
    guess = int(input('What is your guess? '))
    if guess != machine_guess:
        print('Wrooong!')
        guess_try+=1
print('Finally you got the number {}, You got it in {} try(s)'.format(machine_guess, guess_try + 1))




