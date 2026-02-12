#for c in range(1,10,2):
#for c in range(START,FINISH,GO BY X IN X):

#range (0, 3), that do not consider 3, but goes from 0 to 3 (3 spaces)

#Logical Structures for repetition

for c in range(1,6): #that goes 5 times 1 by 1... (1,2,3,4,5)
    print('test')
print('finish')

#Another test... with star and end
for c in range(0,6):
    print(c)

#This will count -1 every step...
for c in range(6, 0, -1):
    print(c)
print('FIM')

#Test 1
n = int(input('Type a number: '))
for b in range (0, n+1):
    print(b)
print('end')

#Test 2
i = int(input('Start number:'))
f = int(input('Ending Number: '))
co = int(input('Counting by: '))
for c in range (i, f+1, co):
    print(c)
print('End!')

#Test 3
s = 0
for c in range(0,4):
    n = int(input('Type a number: '))
    s = s + n # s+= n same thing
print('The sum is {}'.format(s))
