# ======================================================================================================================
# CHALLENGE 79: Unique Values: Read numbers, disconsider not unique values, show all values and set them in order
# ======================================================================================================================

"""
Challenge: 6.2.2 - Unique Values (079)
Category: 6 - Collections
Concepts Used:
    - list()
    - .append()
    - not in
    - while
    - if()
    - else()
    - for
    - end = ''
    - while True
    - break
    - .sort
    - .upper()
    - .strip()

Tags:
Status: ✔️ Completed
"""

#FIRST APPROACH ========================================================================================================

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

#SECOND APPROACH =======================================================================================================

list_numbers = list()
while True:
    n = int(input('Type a value: '))
    if n not in list_numbers:
        list_numbers.append(n)
        print('--- The value was added with success! ---')
    else:
        print(' --- Duplicate ! --- ')
    r = str(input('Do you want to continue? Y/N '))
    if r in 'Nn':
        break
print('-'*60)
list_numbers.sort()
print(f'You typed the values {list_numbers}')
