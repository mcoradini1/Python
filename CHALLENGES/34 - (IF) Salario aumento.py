#ACIMA DE 1250 - 10%, ABAIXO 15%
salario = float(input('Qual e o salario do funcionario? '))
if salario > 1250:
    print('O novo salario apos reajustes e de {} \nUm aumento de 10% '.format(salario+(salario*0.1)))
else:
    print('{:.2f} * 15% = {:.2f}'.format(salario,salario*0.15))
    print('O novo salario apos reajustes e de {} \nUm aumento de 15%'.format(salario+(salario*0.15)))