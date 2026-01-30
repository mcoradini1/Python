#MAKE A PROGRAM TO PRODUCE THE FIBONACCI SEQUENCE, FIRST TERM + SECOND TERM = THIRD THERM
#FIBONACCI SEQUENCE EXAMPLE 0 1 1 2 3 5 8 13 21 34

print('-'*60)
fib = int(input('How many fibonacci numbers do you want? '))
print('-'*60)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end = '')
cont = 3
while cont <= fib:
    t3 = t1 + t2
    print('-> {} '.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> END')


