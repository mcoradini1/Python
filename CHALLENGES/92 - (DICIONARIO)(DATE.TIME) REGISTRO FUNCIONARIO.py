from datetime import datetime
registro = dict ()
registro['NOME'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
registro['IDADE'] = datetime.now().year - nasc
registro['CTPS'] = int(input('Carteira de Trabalho (0 nao tem) '))
if registro['CTPS'] !=0:
    registro['CONTRATACAO'] = int(input('Ano da contratacao: '))
    registro['SALARIO'] = float(input('Salario: R$'))
    registro['APOSENTADORIA'] = registro['IDADE'] + ((registro['CONTRATACAO'] + 35 ) - datetime.now().year)

print('-'*60)
for k,v in registro.items():
    print(f'O {k} e {v}')