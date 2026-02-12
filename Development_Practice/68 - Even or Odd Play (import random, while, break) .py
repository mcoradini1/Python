#PROGRAM A WORD GAME WHERE YOU TYPE A NUMBER AND DECIDE BETWEEN EVEN OR ODD, THE PROGRAM NEEDS TO COUNT:
#HOW MANY CONSECUTIVE VICTORIES AND STOP WHEN I LOSE.

import random
count_victories = 0

while True:
    my_number = int(input('Type a number: '))
    while True:
        my_choice = str(input('Even or Odd? ')).upper()
        if my_choice == 'EVEN' or my_choice == 'ODD':
            break
    computer_num = random.randint(0, 10)
    check = my_number + computer_num
    if check%2 == 0:
        if my_choice == 'EVEN':
            print(f'You WON, you played {my_number}, I played {computer_num} it is {check} that is {my_choice}!\n\n')
            count_victories += 1
        else:
            print(f'You LOSE, the result was {check} what is EVEN and you typed {my_choice}, you had {count_victories} consecutive wins\n\n')
            break

    else:
        if my_choice == 'IMPAR':
            print(f'You WON, you played {my_number}, I played {computer_num} it is {check} that is {my_choice}!\n\n')
            count_victories += 1
        else:
            print(
                f'You LOSE, the result was {check} what is ODD and you typed {my_choice}, you had {count_victories} consecutive wins\n\n')
            break








