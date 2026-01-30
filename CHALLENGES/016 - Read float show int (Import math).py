#AN ALGORITHM TO READ A FLOAD AND SHOW ONLY THE INT
#import math (could use that)
from math import trunc

r = float(input('Enter a float number: '))
print('First method - Your number is -> {}'.format(int(r)))

print('\n\nSecond Method - Your numbers is {} \nIts whole part is {}'.format(r, trunc(r)))

#print('\n\nSecond Method - Your numbers is {} \nIts whole part is {}'.format(r, math.trunc(r)))
#THIS SECOND FORM I WOULD USE IN CASE I HAD IMPORT THE WHOLE LIBRARY MATH