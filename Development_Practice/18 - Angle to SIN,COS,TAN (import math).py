#PROGRAM TO READ AN ANGLE AND PROVIDE THE VALUE FOR SIN, COS, TAN
#import math
from math import sin, cos, tan, radians
angle = float(input('Type the angle: '))

seno = sin(radians(angle))
print('The angle {} has a SIN of {:.2f}'.format(angle, seno))

cose = cos(radians(angle))
print('The angle {} has a COS of {:.2f}'.format(angle, cose))

tan = tan(radians(angle))
print('The angle {} has a TAN of {:.2f}'.format(angle, tan))