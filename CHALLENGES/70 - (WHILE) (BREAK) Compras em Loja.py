total = 0
acima_1000 = 0
mais_barato = ''
mais_barato_valor = 0
while True:
    print('-'*60)
    nome = str(input('Qual o nome do produto? ')).strip().title()
    preco = float(input('Qual o preco '))
    print('-'*60)
    total = total + preco
    if preco >= 1000:
        acima_1000+=1
    if mais_barato_valor == 0:
        mais_barato_valor = preco
        mais_barato = nome
    if mais_barato_valor > preco:
        mais_barato_valor = preco
        mais_barato = nome

    resposta = str(input('Adicionar outro produto? (S/N) ')).strip().upper()
    while True:
        if resposta == 'S' or 'N':
            break
    if resposta == 'N':
        break

print('-'*60)
print(f'\n\nO valor total foi de {total:.2f}\n{acima_1000} produtos custam mais que 1000,00\n{mais_barato} foi o mais barato custando apenas {mais_barato_valor:.2f}')
print('-'*60)