#CREATE A FUNCTION THAT WILL MAKE A CONT AND:
#(A) CONT 1 TO 10,  BY 1
#(B) COUNT 10 TO 0, BY -1
#(C) PERSONALIZED COUNTING

from time import sleep
x = 0 #sleep

def cont_function(beginning,end,rate):
    print(f'A) ', end ='')
    for c in range (0,11):
        print(f'{c}', end =' ')
        sleep(x)
    print(f'\nB) ', end='')
    for b in range (20,-1,-2):
        print(f'{b}', end=' ')
        sleep(x)

    print('\nC) ', end= '')
    if beginning < end:
        if rate == 0:
            rate =1
        print(f'Counting from {beginning} to {end} in the rate of {rate} ')
        for d in range(beginning, end+1, rate):
            print(f'{d} ', end = '')
            sleep(x)

    else:
        if rate == 0:
            rate =1
        print(f'Counting from {beginning} to {end} in the rate of {rate} ')
        for d in range(beginning, end-1, -rate):
            print(f'{d} ', end = '')
            sleep(x)


beginning_type = int(input('\nType the beginning: '))
end_type = int(input('Type the end: '))
rate_type = int(input('Type the rate: '))

cont_function(beginning_type,end_type,rate_type)