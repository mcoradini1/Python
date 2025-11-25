maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('Entre o peso do {} '.format(c)))
    if peso > maior:
        maior = peso
    if menor == 0 or menor > peso:
        menor = peso
print('\nMaior peso -> {:.2f}\nMenor peso -> {:.2f}'.format(maior,menor))