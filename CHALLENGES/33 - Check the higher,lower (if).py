#CHECK THE HIGHER AND LOWER VALUE WITHIN 3 TYPED VALUES
#FIRST APPROACH USING VARIABLES

a = int(input('Type the first number: '))
b = int(input('Type the second number: '))
c = int(input('Type the third number: '))
lower = higher = 0
print (a,b,c)

if a<=c and a<=b:
    lower = a
if b<=a and b<=c:
    lower = b
if c<=a and c<=b:
    lower = c
if a>=b and a>=c:
    higher = a
if b>=a and b>=c:
    higher  = b
if c>=a and c>=b:
    higher = c

print('\n\nThe higher value is {}\nThe lower value is {}'.format(higher, lower))

