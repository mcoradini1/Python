import datetime
hoje = datetime.date.today().year
maior = 0
for c in range (1,8):
    ano = int(input('Digite o ano de nascimento da {} pessoa '.format(c)))
    if hoje - ano >= 18:
        maior += 1
print('Na lista temos: \n{} Maior idade (18+)\n{} Menor idade (18-)'.format(maior,7-maior))