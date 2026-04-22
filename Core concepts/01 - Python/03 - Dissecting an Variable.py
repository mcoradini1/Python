#variable.dissecting-function() <- how most of them work

n = input('Type a number: ')
print(n.isnumeric(), 'for numbers\n')
#This check if it is a number (answer in boolean)

m = input('Type some letters: ')
print(m.isalpha(), 'for letters\n')
#This check if it is alphabetic (answer in boolean)

o = input('Type numbers and letters: ')
print(o.isalnum(), 'for numbers and letters\n')
#This check if it is alphanumeric (answer in boolean)

p = input('Type letters in capitalcase: ')
print(p.isupper(), 'for all letters in CAPITAL\n')
#This check if it is CAPITAL letters (answer in boolean)

q = input('Type lowercase letters: ')
print(q.islower(), 'for lowercase letters\n')

# There are other examples such as isprint, isspace...
