#IMPROVE THE FUNCTION ADDING A RESUME OF ALL FUNCTIONS

def increase(price = 0, tax = 0, use_format = False):
    result = price + (tax*price/100)
    return result if use_format is False else format_coin(result)


def decrease(price = 0, tax = 0, use_format = False):
    result = price + (tax * price / 100)
    return result if use_format is False else format_coin(result)


def twice(price = 0, use_format = False):
    result = price * 2
    return result if use_format is False else format_coin(result)


def half(price = 0, use_format = False):
    result = price / 2
    return result if use_format is False else format_coin(result)


def format_coin(price = 0, coin = '£', perc = ''):
    return f'{coin} {price:.2f} {perc}'.replace('.', ',')

def resume(price = 0, tax_increase = 10, tax_decrease = 10):
    print('-- VALUE RESUME --'.center(40))
    print('-'*40)

    print(f'Product value {format_coin(price)}')
    print(f'The product with an increase of  {format_coin(tax_increase,coin = '', perc = '%')} '
          f'is {increase(price, tax_increase, True)}')

    print(f'The product with an decrease of {format_coin(tax_decrease,coin = '', perc = '%')} '
          f'is {decrease(price, tax_decrease, True)}')

    print(f'The product multiplied by 2 is {twice(price, True)}')
    print(f'The product divided by 2 is {half(price, True)}')

    print('-'*40)
