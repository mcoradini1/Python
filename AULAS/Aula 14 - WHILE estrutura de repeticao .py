#Nao tenho limites neste caso...
#enquanto nao acontecer isto, continua no loop...
#estrutura de repeticao com teste logico
apple = 0
while not apple == 20:
    print('Ainda nao chegou {}'.format(apple))
    apple+=1

while apple < 20:
    print('Outra forma de fazer...\n\n\n')

n = 1
par = impar = 0
while n != 0:
    n=int(input('Digite um valor '))
    if n != 0:
        if n%2 == 0:
            par += 1
        else:
            impar += 1
print('pares {}\nimpares {}'.format(par,impar))

