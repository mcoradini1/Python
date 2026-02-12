#A PROGRAM TO SHOW NUMBERS FROM 0 TO 50, BUT ONLY EVEN ONES
for c in range (0, 52):
    if c%2 == 0:
        print(c, end=',')
print('\n')

for c in range (0, 51, 2):
    print(c, end=' ')
