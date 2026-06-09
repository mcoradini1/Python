#variable.dissecting-function() <- how most of them work

n = input('Type a number: ')
print(n.isnumeric(), '5.1 - For numbers\n')
#This check if it is a number (answer in boolean)

m = input('Type some letters: ')
print(m.isalpha(), '5.1 - For letters\n')
#This check if it is alphabetic (answer in boolean)

o = input('Type numbers and letters: ')
print(o.isalnum(), '5.1 - For numbers and letters\n')
#This check if it is alphanumeric (answer in boolean)

p = input('Type letters in capitalcase: ')
print(p.isupper(), '5.1 - For all letters in CAPITAL\n')
#This check if it is CAPITAL letters (answer in boolean)

q = input('Type lowercase letters: ')
print(q.islower(), '5.1 - For lowercase letters\n')

# There are other examples such as isprint, isspace...
