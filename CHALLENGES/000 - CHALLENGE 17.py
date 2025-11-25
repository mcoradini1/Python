#Programa para ler cateto oposto e adjacente e achar o valor da hipotenusa
import math

co = float(input('Entre o valor do cateto oposto: '))
ca = float(input('Entre o valor do cateto adjacente: '))
h = (ca**2+co**2)**(1/2)
print ('A hipotenusa vale: {:.2f}'.format(h))

print('A hipotenusa vale {:.2f}'.format(math.hypot(co,ca)))


