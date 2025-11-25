matriz = [[], []]
linhas = 0
colunas = 0

#toda vez que colunas == 3 linhas vai para +1
for colunas in range(0,3):
    matriz[linhas].append(int(input(f'Digite o valor ({linhas}{colunas})')))

    if colunas == 3:
        linhas+=1

    if colunas == 3 and linhas == 3:
        break


print(matriz)