"""
5.2 - While: Structure Of Repetition with logical test good when we do not know exactly how many iterations will take
Here the is no limits, while something does not happen it will continue the repetition unless using BREAK.

while test:
    loop

while not test:

while variable in ('a,b,c'):

while True: (will be infinite loop)

break
used to break infinite loops

"""

#Example 1 ---------------------------------------
apple = 0
while not apple == 20:
    print('We still don`t have enough {}'.format(apple))
    apple+=1

while apple < 20:
    print('That`s another way o do it...\n\n\n')


#Example 2 ---------------------------------------
n = 1
even = odd = 0
while n != 0:
    n=int(input('Type a value (0 closes): '))
    if n != 0:
        if n%2 == 0:
            even += 1
        else:
            odd += 1
print('evens: {}\nodds: {}'.format(even,odd))


#Example 3 (break)---------------------------------

while True:
    print('infinite loop')
    break


#Example 4 (break)--------------------------------

n = s = m = 0

while True:
    n = int(input('Type a number '))
    if n == 999:
        break
    s += n
    m+=1
print('Numbers typed {} (disconsidering 999)'.format(m))
print(f'The sum is {s}')