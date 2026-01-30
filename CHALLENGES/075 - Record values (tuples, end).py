#PROGARM TO RECEIVE 4 VALUES AND RETURN:
#COUNT OF 9, WHICH POSITION WAS 3, EVEN VALUES

i = (int(input('Type a number: ')),
     int(input('Type another number: ')),
     int(input('Type another number: ')),
     int(input('Type another number: ')))

print(i)
print(f'-> The number 9 appeared {i.count(9)}')
if 3 in i:
    print(f'-> The number three appeared the first time at {i.index(3)+1} positon')
else:
    print('-> The number three did not appear at all')
print('-> The pair numbers are: ')

for n in i:
    if n % 2 == 0:
        print(n, end = ' ')


