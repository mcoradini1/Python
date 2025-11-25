# while true: (vai sempre repetir se nao houver um termo de parada)
n = s = 0

while True:
    n = int(input('Digite um numero '))
    if n == 999:
        break
    s += n
print('A soma e {}'.format(s))
print(f'A soma e {s}')