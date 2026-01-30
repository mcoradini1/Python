#ALGORITHM TO READ ADJACENT SIDE, OPPOSITE SIDE AND FINDS HYPOTENUSE
import math

co = float(input('Enter the opposite side: '))
ca = float(input('Enter the adjacent side: '))
h = (ca**2+co**2)**(1/2)
print ('The Hypotenuse is {:.2f}'.format(h))

print('The Hypotenuse is {:.2f}'.format(math.hypot(co,ca)))


