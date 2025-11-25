#LEITOR D IMC
valor = float(input('Entre o valor da compra '))
print('''As formas de pagamento sao:

[1] A vista dinheiro (10% de desconto)
[2] A vista cartao (5% de desconto)
[3] Em 2x (Mesmo preco)
[4] 3x ou mais (extra 20%)
''')
fpag = int(input('Qual forma de pagamento? '))

if fpag == 1:
    print('Sua compra ficou {:.2f} R$ a vista '.format(valor*0.9))
elif fpag == 2:
    print('Sua comrpra ficou {:.2f} R$ a vista no cartao'.format(valor*0.95))
elif fpag == 3:
    print('Sua compra ficou {:.2f} R$, em 2 parcelas de {:.2f}'.format(valor, valor/2))
elif fpag ==4:
    parcela = int(input('Em quantas vezes vai fazer? '))
    print('Sua compra ficou em {:.2f} R$, em {} parcelas de {:.2f}'.format(valor*1.2, parcela, valor*1.2/parcela))

