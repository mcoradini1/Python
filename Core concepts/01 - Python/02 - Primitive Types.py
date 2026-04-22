#Remember of objetive: 01 - Python course oriented to object is great to generate graphic interface

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
n3 = ('potato')
print(type(n3), n3, s)



#DYNAMIC Tipping
x = 3   #create first object 3, then create first variable x and insert the reference for the object
y = x   #object x already exists, create a new variable y and then reference an object
y = y - 1 #remove the reference from 3, to 2...

l1 = [1,2,3] #createthe first object [1,2,3] list and assign it to L1
l2 = l1 #assign the object to this variable creating a bond with then
l1[0] = 24 #both l1 and l2 are equal...
l1 == l2 #true
l1 is l2 #true

#id shows a unique number of a storaged object, mutable objects can be identical in content but be different objects.
id(l1) == id(l2) #true


m1 = [1,2,3,4,5]
m2 = [1,2,3,4,5]
m1 == m2  #true
m1 is m2 #false

id(m1) == id(m2) #false


