#PROGRAM A GUESS GAME LIKE 028, BUT NOW WE CAN GUESS FROM 0 TO 10 AND TILL GET IT RIGHT

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




