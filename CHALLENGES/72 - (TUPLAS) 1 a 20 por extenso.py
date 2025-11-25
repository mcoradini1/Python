tup = ('zero', 'um', 'dois', 'tres', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinte', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    i = int(input('Entre um numero de 0 a 20 '))
    if 0 <= i <= 20:
        break
    print('Tente Novamente,', end = '')

print(f'Voce digitou {tup[i]}')