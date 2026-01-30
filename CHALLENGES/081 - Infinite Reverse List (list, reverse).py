#PREPARE A INFINITE LIST WITH STOP CRITERIA, SHOW THE LIST FROM THE HIGHER TO LOWER
#TELL IF THE NUMBER 5 IS FOUND WITHIN TE LIST

list_infinite = list ()
while True:
    list_infinite.append(int(input('Type a number: ')))
    r = str(input('Do you want to continue? Y/N'))
    if r in 'Nn':
        break
list_infinite.sort(reverse = True)
print(' - '*60)
print(f'[{len(list_infinite)}] Numbers typed\nThe values inside the list are: {list_infinite}')
if 5 in list_infinite:
    print('The value 5 was FOUND in the list')
else:
    print('The value 5 was NOT FOUND in the list')

