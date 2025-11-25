boletim = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome,[nota1, nota2], media])
    r = str(input('Deseja continuar? S/N: '))
    while r not in 'nNsS':
        r = str(input('Deseja continuar? S/N: '))
    else:
        if r in 'Nn':
            break

print('-'*60)
print(f'{'Numero':<14}{'Nome':<14}{'Media':<14}')
print('-'*60)
for i, i1 in enumerate(boletim):
    print(f'{i:<14}{i1[0]:<14}{i1[2]:<14}')
print('-'*60)

while True:
    v=int(input('Qual aluno voce gostaria de ver as notas? (999 interrompe): '))
    if v == 999:
        break
    if v <= len(boletim) - 1:
        print(f'As notas de {boletim[v][0]} sao {boletim[v][1]}')

print('ACABOU')