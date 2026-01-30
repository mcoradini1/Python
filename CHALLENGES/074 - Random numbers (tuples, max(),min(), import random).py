#A PROGRAM THAT WILL RANDOMLY GENERATE 5 VALUES (FROM 0 TO 999), AND CHOSE THE HIGHER AND LOWER

from random import randint
i = [randint(0,999),randint(0,999),randint(0,999), randint(0,999),randint(0,999)]
print(i)
print(f'The higher value is {max(i)}')
print(f'The lower value is {min(i)}')