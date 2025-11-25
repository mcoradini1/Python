#checar se a pessoa tem que se alistar ou nao para o exerxito
from datetime import date
hoje = date.today().year
nascimento = int(input('Entre o ano que voce nasceu '))
idade = hoje - nascimento
print (idade)
if idade == 18:
    print('Voce precisa se alistar esse ano')
elif idade < 18:
    print('Voce esta novo para se alistar')
else:
    print('Seu alistamento foi a {} anos'.format(idade - 18))