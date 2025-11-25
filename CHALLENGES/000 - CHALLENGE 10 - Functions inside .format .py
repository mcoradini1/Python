#Programa que ve quanto dinheiro a pessoa tem, e quanto ela pode trocar em dollares 1 dollar = 3.27 reais
n = float(input('Entre a quantidade de dinheiro que tens na carteira '))
d = 3.27
m1 = n/d
m2 = n//d
m3 = m1 - m2
m4 = m3 * d

print('Voce pode comprar {}, e vai te sobrar {:.3f} reais'.format(m2,m4))
print('\n\nNuma forma mais simples voce pode comprar {:.3f}'.format(n/d))