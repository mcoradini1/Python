# Viagem curta (ate 200 km = 50 cents), viagem longa 45 cents
distancia = float(input('Entre a distancia da viagem '))
if(distancia <= 200):
    valor = distancia * 0.50
    print('O preco da sua viagem vai ficar {:.2f} R$'.format(valor))
else:
    valor = distancia * 0.45
    print('O preco da sua viagem vai ficar {:.2f} R$'.format(valor))

# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45