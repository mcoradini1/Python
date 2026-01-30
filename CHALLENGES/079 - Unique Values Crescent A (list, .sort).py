#A PROGRAM TO READ NUMBERS, DISCONSIDER WHEN THEY ARE REPEATED AND IN THE END SHOW THE ORDER THAT WAS SAID AND
#THE UNIQUE NUMBERS, IN THE END SET THE VALUES IN CRESCENT ORDER.

list_complete = list()
list_unique = list()
answer = 'Y'
while answer == 'Y':
    list_complete.append(int(input('Type a number: ')))
    if list_complete[-1] not in list_unique:
        list_unique.append(list_complete[-1])
    else:
        print('We already have this number, I will disconsider it.')

    answer = str(input('Do you want to continue? Y/N ')).upper()


    while answer != 'Y' and answer != 'N':
        answer = input('INVALID!\nDo you want to continue? Y/N ').upper().strip()

list_unique.sort()
print(f'{list_complete} e {list_unique}')

for count in list_unique:
    print(f'{count}', end = ' -> ')
print('FIM')

