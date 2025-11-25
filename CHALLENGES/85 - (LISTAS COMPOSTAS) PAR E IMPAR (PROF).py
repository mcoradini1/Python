lista_geral = [[], []]

for c in range (1,8):
    a = int(input(f'Insira o {c} numero '))
    if a % 2 == 0:
        lista_geral[0].append(a)
    else:
        lista_geral[1].append(a)

lista_geral[0].sort()
lista_geral[1].sort()

print(f'PARES {lista_geral[0]} e os IMPARES {lista_geral[1]}')