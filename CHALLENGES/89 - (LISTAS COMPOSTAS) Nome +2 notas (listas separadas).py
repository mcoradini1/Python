boletim = [[],[]]
alunos = list ()
notas = list()

while True:
    print('-'*60)
    alunos.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Notas 2: ')))
    print('-'*60)
    r = str(input('Quer continuar? S/N '))
    while r not in 'SsNn':
        r = str(input('Quer continuar? S/N '))
    if r in 'Nn':
        break
boletim[0].append(alunos[:])
boletim[1].append(notas[:])

for n in range (0,len((boletim[1]))):
    print('n')
