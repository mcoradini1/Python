#PROGRAM THAT WILL RECEIVE NAME, SEX AND AGE OF SOME PEOPLE AND STORE IT IN DICTIONARIES/LISTS

everybody = list()
person = dict()
sum_age = 0
while True:
    person.clear() #HERE IN THE BEGINNING I CLEAN THE DICTIONARY FOR THE NEXT CYCLE.
    person['name'] = str(input('Name: ')).title()
    while True:
        person['sex'] = str(input('Sex [M/F] ')).upper()[0]
        if person['sex'] in 'MF':
            break
        print('ERROR! Please type M or F')
    person['age'] = int(input('Age: '))
    sum_age+= person['age']
    everybody.append(person.copy()) #HERE I ADD THE DICTIONARY INSIDE THE LIST (WITH APPEND AND COPY TO NOT CREATE BONDS)
    while True:
        answer = str(input('Do you want to continue? [Y/N] ')).upper()[0]
        if answer in 'YN':
            break
        print('ERROR! Answer only with Y ou N.')
    if answer == 'N':
        break
print('-'*60)
media = sum_age / len(everybody)
print(f'A) People entered {len(everybody)}')
print(f'B) Average of ages are {media:5.2f}') #2 DECIMALS ONLY
print(f'C) Women registered are ', end='')
for p in everybody:
    if p['sex'] in 'Ff':
        print(f'{p['name']}', end = ' ')
print()
print(f'D) People above the average ', end='')
print()
for t in everybody:
    if t['age'] > media: #I COULD HAVE DONE THE SAME AS BEFORE, JUST TESTING THIS WAY
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')








