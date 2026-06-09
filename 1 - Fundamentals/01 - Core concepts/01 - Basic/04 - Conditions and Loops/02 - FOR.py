"""
5.1 - For: Laces, Repetitions, Iterations.

Logical Structures 5.1 - For repetition (Good if I have a target and know how many iterations I need)

example:
5.1 - For c in range(1,10,2):
5.1 - For c in range(Start, end, step):

range (0, 3), that do not consider 3, but goes from 0 to 3 (0,1 and 2)

"""

for c in range(1,6): #that goes 5 times 1 by 1... (1,2,3,4,5)
    print('test', c)
print('finish')

#This will count -1 every step...
for c in range(6, 0, -1):
    print(c)
print('END')

#Example 1
n = int(input('Type a number: '))
for b in range (0, n+1):
    print(b)
print('END')

#Example 2
i = int(input('Start number:'))
f = int(input('Ending Number: '))
co = int(input('Counting by: '))
for c in range (i, f+1, co):
    print(c)
print('END')

#Example 3
s = 0
for c in range(0,4):
    n = int(input('Type a number: '))
    s = s + n # s+= n same thing
print('The sum is {}'.format(s))
