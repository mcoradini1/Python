dict_people = {'name':'marlon', 'age' : 31, 'weight': 90 }
database = list()

print(dict_people)
print('\n')
for k in dict_people.keys():
    print(f'{k}')
print('\n')
for k in dict_people.values():
    print(f'{k}')
print('\n')
for k, v in dict_people.items():
    print(f'{k} is {v}')
print('\n')

database.append(dict_people.copy())
dict_people = {'name':'susana', 'age' : 29, 'weight': 65 }
database.append(dict_people.copy())
dict_people = {'name':'anabela', 'age' : 50, 'weight': 70 }
database.append(dict_people.copy())

print(database[0]['weight'])
print(database)
print('\n')

for k in database:
    print(f'{k}')
    for v, b in k.items():
        print(f'{v} is {b}')
    print('\n')
