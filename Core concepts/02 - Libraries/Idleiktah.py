valor = 3543
increase_daily = 0.1
days = int(input('Tell how many days to consider: '))

print(f'Valor today = {valor}')

for i in range(days):
    valor = valor + (valor * increase_daily)
    print(f'Valor day {i} = {valor:.2f} an increase of {valor * increase_daily:.2f}')