from time import sleep
sleep_time = 0.3

def higher_func(*num):
    print('-'*60)
    higher1 = 0
    for value in num:
        print(f'{value} ', end='')
        sleep(sleep_time)
        if value >= higher1:
            higher1 = value
    print(f'\nThe highest value is {higher1}')
    print('-'*60)


higher_func(1, 2, 3, 4, 5, 6)
higher_func(2, 4, 7, 0, 124, 5, 32, 8, 0)
higher_func(1, 2, 2, 2, 3, 4, 6, 9, 98, 675)