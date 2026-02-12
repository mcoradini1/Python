#ANOTHER APPROACH FOR THE SAMPLE 79A.
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


