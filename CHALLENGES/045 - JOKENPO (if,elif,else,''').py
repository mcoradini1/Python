#PROGRAM A JOKENPO GAME
import random

print('''---------Welcome to The JoKenPo Game---------
[1] Stone
[2] Paper
[3] Scissors

''')

machine_choice = random.choice([1, 2, 3])
choice = int(input('Your choice: -> '))


if choice == machine_choice:
    print('DRAWWWW!')
elif choice == 1 and machine_choice ==2:
    print('You LOSE, I played PAPER')
elif choice ==1 and machine_choice ==3:
    print('You WIN, I played SCISSORS')
elif choice == 2 and machine_choice ==1:
    print('You WIN, I played STONE')
elif choice == 2 and machine_choice == 3:
    print('You LOSE, I played SCISSORS')
elif choice ==3 and machine_choice ==1:
    print('You LOSE, I played STONE')
elif choice ==3 and machine_choice ==2:
    print('You WIN, I played PAPER')
