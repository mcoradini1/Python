t = int(input('ENTRE O TERMO DA PA '))
r = int(input('ENTRE A RAZAO DA PA '))
resultado = t
t10=0
while not t10 == 11:
    print(resultado,end=' -> ')
    t10+=1
    resultado = resultado + r

t_extra = 1
t_extra_count = 0
while t_extra != 0:
    t_extra = int(input('FIM\n\nQuantos termos extra voce gostaria de ver? '))
    t_extra_count = 0
    while not t_extra_count == t_extra:
        t_extra_count+=1
        resultado = resultado + r
        print(resultado, end = ' -> ')

print('\n\nENCERRANDO O SISTEMA')



'''t_extra=int(input('FIM!\n\n Quantos termos extras voce gostaria de ver? '))
t_extra_count = 0
if t_extra == 0:
    print('\n\nENCERRANDO O SISTEMA')
else:
    while t_extra != t_extra_count:
        print(resultado, end=' -> ')
        t_extra_count+=1
        resultado = resultado + r
print('FIM')'''