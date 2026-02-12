list_numbers = list()

for c in range (0,5):
    a = int(input('Type a number: '))
    if c == 0:
        list_numbers.append(a)
        print('It is added to the end of the list')
    elif a > list_numbers[-1]: #lista[len(lista)-1] COULD BE LIKE THAT
        # [-1] DEMONSTRATE FIRST VALUE FROM RIGHT TO LEFT
        list_numbers.append(a)
        print('It is added to the end of the list')
    else:
        position = 0
        while position < len(list_numbers):
            if a <= list_numbers[position]:
                list_numbers.insert(position, a)
                print(f'Add in the position {position}')
                break

print(f'The list is {list_numbers}')


#WAY TO JOIN THEM
#if c ==0 or a > list_numbers [-1]:
    #list_numbers.append(a)


