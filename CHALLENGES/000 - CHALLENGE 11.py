#Ler largura e altura de parede e dizer quantos m2 de tinta vai ser necessario. (1 lata pinta 2m2)
l = float(input('Entre a Largura da parede '))
a = float(input('Entre a altura da parede '))


print('A parede tem {} m2'.format(l*a))
print('Para pintar esta parede sera necessario {:.0f} latas'.format(l*a/2))
