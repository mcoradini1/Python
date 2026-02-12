import coins
p = float(input('Type your price: £'))
print(f'2x the price is £{coins.twice(p)}')
print(f'Half of the price is £{coins.half(p)}')
print(f'Increasing the price by 10% I would have £{coins.increase(p, 10)}')
print(f'Decreasing the price by 10% I would have £{coins.decrease(p, 10)}')

