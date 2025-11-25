#VARIAVEIS COMPOSTAS QUE SAO IMUTAVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[3]) #o terceiro termo e Pudim, pois o termo 0 e Hamburguer
print(lanche[1:3]) # fatiamento mostra o dentro do intervalo desconsiderando o termo final...

print('\n\n')

for comida in lanche:
    print(f'Vou comer {comida}')
print('Comi demais')


print('\n\n')


for cont in range(0, len(lanche)):
    print(lanche[cont])


print('\n\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('\n\n')

print(sorted(lanche)) # por em ordem alfabetica