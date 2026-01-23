nome = str(input('Whats your name? ')).strip()
print(nome) #just to check
nome = nome.capitalize()
print(nome) #Just checking capitalize
if nome == 'Marlon':
    print('What a beautiful name {}'.format(nome))
else:
    print('Your name is cool {}'.format(nome))
print('Good Morning {}!'.format(nome))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: