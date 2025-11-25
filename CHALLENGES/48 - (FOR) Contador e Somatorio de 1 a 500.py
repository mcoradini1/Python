somatorio = 0
contador = 0
for c in range (0,501):
    if c%2 != 0 and c%3 == 0:
        somatorio = somatorio + c
        contador = contador + 1
        #contador+= 1
        print(somatorio, end=' ')
print('\n')
print(contador)
