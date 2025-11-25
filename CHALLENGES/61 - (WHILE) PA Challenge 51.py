t = int(input('ENTRE O TERMO DA PA '))
r = int(input('ENTRE A RAZAO DA PA '))
resultado = t
t10=0
while not t10 == 11:
    print(resultado,end=' -> ')
    t10+=1
    resultado = resultado + r
print('FIM')