lista_geral = list ()
lista_par = list ()
lista_impar = list ()

for c in range (0,7):
    a = int(input(f'Insira o {c+1} numero '))
    if a % 2 == 0:
        lista_par.append(a)
        print('par')
    else:
        lista_impar.append(a)
        print('impar')
lista_par.sort()
lista_impar.sort()
lista_geral.append(lista_par[:])
lista_geral.append(lista_impar[:])


print(f'PARES {lista_geral[0]} e os IMPARES {lista_geral[1]}')