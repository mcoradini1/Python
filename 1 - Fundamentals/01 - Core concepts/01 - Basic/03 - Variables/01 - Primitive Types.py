"""
----------------------------------------- Primitive Types --------------------------------------------------------------
float: similar o real numbers
int: number without decimals
str: strings (text)
bool: true or false

----------------------------------------- Dynamic Type -----------------------------------------------------------------

Single Variables:
x = 3   (create first object 3, then create first variable x and insert the reference 5.1 - For the object)
y = x   (object x already exists, create a new variable y and then reference an object)
y = y - 1 (remove the reference from 3, to 2...)


l1 = [1,2,3] (create the first object [1,2,3] list and assign it to L1)
l2 = l1 (assign the object to this variable creating a bond with then)
l1[0] = 24 (both l1 and l2 are equal...)
l1 == l2 (true)
l1 is l2 (true)

---------------------------------- id (shows number of identification in memory ----------------------------------------
id(l1) == id(l2)

"""

n1 = 10
n2 = 5
n3 = 'Potato'
s = n1 + n2


print('The sum between {} and {} is equal to {}'.format(n1,n2,s))
print(type(s))
print(type(n3))


m1 = [1,2,3,4,5]
m2 = [1,2,3,4,5]

print(m1 == m2)

#these two are similar:
print(m1 is m2)
print(id(m1) == id(m2))


