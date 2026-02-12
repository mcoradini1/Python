#PROGRAM TO RECEIVE A NUMBER AND DIVIDE IT INTO UNITS, TENS, HUNDREDS, THOUSANDS

#1 - APPROACH - CONSIDERING THAT EVERY STRING IS A LIST OF LETTERS, WE CAN TREAT IT AS A LIST
#THIS IS PROBLEMATIC BECAUSE, ANY NUMBER BIGGER THAN 1000 WILL BREAK THE PROGRAM.

num = int(input('Type a number: '))
n = str(num)
print('Analyzing the number {}'.format(num))
print('Unit: {}'.format(n[3]))
print('Tens: {}'.format(n[2]))
print('Hundreds: {}'.format(n[1]))
print('Thousands: {}'.format(n[0]))

#2 - APPROACH - THIS IS MORE RELIABLE
print('\n\n--------------------------------')
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
print('Units: {}'.format(u))
print('Tens: {}'.format(t))
print('Hundreds: {}'.format(h))
print('Thousands: {}'.format(th))