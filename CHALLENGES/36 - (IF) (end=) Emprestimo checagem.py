#o valor da prestacao mensal nao pode ser maior que 30% do salario
casa = float(input('Qual e o preco da casa? '))
salario = float(input('Qual e o salario mensal da familia? '))
financiamento = int(input('Em quantos anos vai ser pago? '))
parcelas = casa / (financiamento * 12)
if parcelas > 0.3 * salario:
    print('Emprestimo NEGADO, sua parcela e de {:.2f} R$, superior a 30% do seu salario ({:.2f} R$)'.format(parcelas,salario * 0.3))
else:
    print('Emprestimo APROVADO, sua parcela sera de {:.2f} R$, inferior a 30% do seu salario ({:.2f} R$)'.format(parcelas, salario * 0.3))
    print('Testando hihi', end='-'*8)
    print('teste 3')