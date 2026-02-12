import coins
p = float(input('Type your price: £'))
print(f'2x the price is {coins.format_coin(coins.twice(p))}')
print(f'Half of the price is {coins.format_coin(coins.half(p))}')
print(f'Increasing the price by 10% I would have {coins.format_coin(coins.increase(p, 10))}')
print(f'Decreasing the price by 10% I would have {coins.format_coin(coins.decrease(p, 10))}')

