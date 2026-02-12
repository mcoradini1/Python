#PROGRAM TO CALCULATE A FACTORIAL NUMBER USING WHILE OR FOR:
#APPROACH 1: WHILE
n = int(input('Type a number '))
factorial = n
n1 = n
while not n == 1:
    factorial = factorial * (n - 1)
    n-=1
print(factorial)

#APPROACH 2: FOR
n1 = int(input('\n\n\nType another number '))
factorial1 = n1

for c in range (n1,1,-1):
    factorial1 = factorial1 * (n1 - 1)
    n1-=1
print(factorial1)