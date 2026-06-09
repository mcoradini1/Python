"""
TUPLES — Python Fundamentals

- Ordered
- Immutable
- Allow duplicates
- Faster than lists
- Defined with () or tuple()
"""

# ---------------------------------------------------------
# CREATING TUPLES
# ---------------------------------------------------------

t1 = ()
t2 = tuple()
t3 = (1, 2, 3)
t4 = 1, 2, 3                # tuple without parentheses

# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------

t = ('apple', 'banana', 'cherry')
print(t[0])

# ---------------------------------------------------------
# PACKING & UNPACKING
# ---------------------------------------------------------

person = ('John', 30)
name, age = person
print(name, age)

# ---------------------------------------------------------
# IMMUTABILITY
# ---------------------------------------------------------

# t[0] = 'new'  # ERROR: tuples cannot be changed

# ---------------------------------------------------------
# TUPLES IN PRACTICE
# ---------------------------------------------------------

# Useful 5.1 - For fixed data, coordinates, database rows, etc.
point = (10, 20)
print(point)


# ---------------------------------------------------------
# EXAMPLE 1:
# ---------------------------------------------------------

Snack = ('Hamburger', 'Juice', 'Pizza', 'Pudim')
print(Snack)
print(Snack[3]) #The third term is PUDIM, because HAMBURGUER is the term 0
print(Snack[1:3]) #Cutting not considering the last term, starts on Juice and finishes on Pizza)
print(sorted(Snack)) #To put it in alphabetic order (it does not change Snack Tuple, just print it sorted)

print('\n')

for food in Snack:
    print(f'I will eat {food}')
print('I ate to much!')

print('\n')

for cont in range(0, len(Snack)):
    print(Snack[cont])


print('\n')

for pos, food in enumerate(Snack): #when use enumerate I have to use 2 variables here...
#first term pos is position, and food is the content of the variable...

    print(f'I will eat {food} in the position {pos}')

print('\n')


# ---------------------------------------------------------
# EXAMPLE 2:
# ---------------------------------------------------------

a = (2,4,6)
b = (1,3,5)
c = a + b #IT WILL JOIN BOTH A and B. (2,4,6,1,3,5)
print(c)
print(sorted(c)) #PUT C IN ORDER, it will not change the variable C...
print(c.count(6)) #how many numbers 6 I have....
print(c.index(2)) #the position of number 2

(c1,c2,c3) = b
print(c1)
print(c2)
print(c3)
