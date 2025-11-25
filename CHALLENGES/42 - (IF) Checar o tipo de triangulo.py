#Checar se um triangulo e EQUILATERO, ESCALENO OU ISOSCELES,
r1 = float(input('Entre o primeiro segmento de reta '))
r2 = float(input('Entre o segundo segmento de reta '))
r3 = float(input('Entre o terceiro segmento de reta '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO, todos lados iguais')
    elif r1 != r2 != r3:
        print('ESCALENO, todos lados diferentes')
    else:
        print('Isosceles, dois lados iguais ')

else:
    print('Os segmentos nao podem formar um triangulo')