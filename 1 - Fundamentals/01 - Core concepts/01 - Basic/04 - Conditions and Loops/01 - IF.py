"""
if(condition 1):
    answer

elif(condition ...):
    answer

elif not in ('a','b','c'):
    answer

else:
    answer

"""

#Simple Application:

nome = str(input('Whats your name? ')).strip()
print(nome) #just to check
nome = nome.capitalize()

print(nome) #Just checking capitalize
if nome == 'Marlon':
    print('What a beautiful name {}'.format(nome))
else:
    print('Your name is cool {}'.format(nome))
print('Good Morning {}!'.format(nome))
