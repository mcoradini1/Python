#eSCREVER UM PROGRAMA QUE LE A VELOCIIDADE (ACIMA DE 80 MULTA, a multa e 7 reais por km acima do limite)
velocidade = float(input('Qual e a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce foi multado e deve pagar {:.2f} R$'.format(multa))
else:
    print('Voce nao foi multado')
print('\n\nTenha um bom dia ')