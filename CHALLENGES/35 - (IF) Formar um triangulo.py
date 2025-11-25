#Se as 3 retas podem formar um triangulo
print('-='*20)
print('        Analisador de Triangulos')
print('-='*20)
r1 = float(input('\nEntre a primeira medida '))
r2 = float(input('Entre a segunda medida '))
r3 = float(input('Entre a terceira medida '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima NAO podem formar um triangulo')