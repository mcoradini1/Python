import random

#We model what we can and the rest is randomness attributed

#HEAD OR TAIL ----------------------------------------------------------------------------------------------------------
print(random.choice(['H', 'T']))  #HEAD or TAIL
print(random.choice(['1', '0']))

#ROLL A DIE ------------------------------------------------------------------------------------------------------------
print(random.choice([1,2,3,4,5,6]))
print(random.choice(range(1,7)))

print(random.choice([range(1,7), range(1,9), range(1,11)]))

print('\n\n')
x = 0
count_x = 0
while count_x != 10:
    x = random.choice(random.choice([range(1,7), range(1,9), range(1,11)]))
    print(x)
    count_x += 1
print(count_x)



