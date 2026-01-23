#Remember of objetive: Python course oriented to object is great to generate graphic interface

#Primitive Types (4 types, more used) - int, str, float, bool...
#float: similar o real numbers
#int: number without decimals
#str: strings (text)
#bool: true or false

print('==========Challenge 1==========')
n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
s = n1 + n2
print('\nThe sum between {} and {} is equal to {}'.format(n1,n2,s))

#print('#1 The sum is equal to ',s)
#print('#2 The sum is equal to {}'.format(s))
#print('A soma entre {0} e {1} vale {2}'.format(n1,n2,s))
# Here three other ways to do the same thing.

print('\nNow one example to show the type of variable use for the result of the sum:')
print(type(s))

print('\n=========Another Example============')
n3 = ('batata')
print(type(n3), n3, s)




