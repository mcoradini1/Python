aluno = dict ()
aluno['nome'] = str(input('De o nome: ')).title()
aluno['nota'] = float(input(f'De a nota do {aluno['nome']} '))

if aluno['nota'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 >= aluno ['nota'] < 7:
    aluno['situacao'] = 'RECUPERACAO'
else:
    aluno['situacao'] = 'REPROVADO'
print('\n')
print('-'*30)

for k, c in aluno.items():
    print(f'{k} -> {c}')