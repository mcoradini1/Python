general_list = list ()
people = list ()
weight_higher = weight_lower = 0
print('-'*60)
while True:
    people.append(str(input('Name: ')))
    people.append(int(input('Weight: ')))

    if len(general_list) == 0:
        weight_higher = weight_lower = people[1]
    if people[1] > weight_higher:
        weight_higher = people[1]

    if people[1] < weight_lower:
        weight_lower = people[1]

    general_list.append(people[:])
    people.clear()
    r = str(input('Do you want to continue? Y/N'))
    if r in 'Nn':
        break
    elif r in 'Yy':
        print('-'*60)
    else:
        r = str(input('Invalid!\nDo you want to continue? Y/N'))
print('-'*60)
print(f'The amount of registered people is/are {len(general_list)}')

print(f'Higher weight {weight_higher}', end =' ')

for c in range(0, len(general_list)):
    if general_list[c][1] == weight_higher:
        print(f'{general_list[c][0]}', end =' ')

print(f'\nLower weight {weight_lower}', end =' ')

for b in range(0, len(general_list)):
    if general_list[b][1] == weight_lower:
        print(f'{general_list[b][0]}', end =' ')




