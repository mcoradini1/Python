# Aluguel de carro por Km (0.65 cents) e (60 reais por dia)
kmd = float(input('Quantos km foram rodados com o carro? '))
diad = float(input('Quantos dias com o carro? ') )
km = 0.65
dia = 60

print('Voce rodou {} km em {} dias? '.format(kmd,diad))

print('O valor total a pagar ficou em R$ {:.2f}'.format((km*kmd)+(diad*dia)))


