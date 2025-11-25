matriz = [[0,0,0], [0,0,0], [0,0,0]]
par_sum = 0
colunas3 = 0
maior2 = 0

for linhas in range (0,3):
    for colunas in range (0,3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas}, {colunas}] '))
print('=-'*60)

for linhas in range (0,3):
    for colunas in range(0, 3):
        if matriz[linhas][colunas] % 2 == 0:
            par_sum = par_sum + matriz[linhas][colunas]

for linhas in range (0,3):
    colunas3 = colunas3 + matriz[linhas][2]

for colunas in range (0,3):
    if matriz[1][colunas] > maior2:
        maior2 = matriz[1][colunas]

for linhas in range (0, 3):
    for colunas in range(0,3):
        print(f'[{matriz[linhas][colunas]:^5}]', end = ' ')
    print()

print(f'A soma total dos pares deu {par_sum}\nA soma da terceira coluna deu {colunas3}\nE o maior valr da segunda linha e {maior2} ')
