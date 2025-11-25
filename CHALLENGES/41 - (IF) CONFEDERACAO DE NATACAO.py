#ATE 9 ANOS MIRIM ATE 14 ANOS INFANTIL ATE 19 UUNIOR ATE 25 SENIIOR MAIOR MASTER

idade = int(input('Qual a sua idade? '))
if idade < 9:
    print('O candidato e considerado MIRIM (Menor que 9 anos)')
elif 9 < idade < 14:
    print('O candidato e considerado INFANTIL (Entre 9 e 14 anos)')
elif 14 <= idade < 19:
    print('O candidato e considerado JUNIOR (Entre 14 e 19 anos)')
elif 19 <= idade < 25:
    print('O candidato e considerado SENIOR (Entre 19 e 25 anos)')
else:
    print('O candidato e considerado MASTER (Acima de 25 anos) ')
