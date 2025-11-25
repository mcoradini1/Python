#PROGRAMA PARA LER UM ANGULO E DAR VALOR DE SENO COS E TAN
#import math
from math import sin, cos, tan, radians
angulo = float(input('Entre o valor do angulo: '))

seno = sin(radians(angulo))
print('O angulo {} tem um SEN de {:.2f}'.format(angulo,seno))

cose = cos(radians(angulo))
print('O angulo {} tem um COS de {:.2f}'.format(angulo,cose))

tan = tan(radians(angulo))
print('O angulo {} tem uma TAN de {:.2f}'.format(angulo, tan))