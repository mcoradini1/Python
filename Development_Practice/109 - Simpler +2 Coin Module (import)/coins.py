#IMPROVE THE FUNCTION A BIT MORE TO BE MORE READABLE, MAKING THE FORMAT AN INTERNAL FUNCTION OF COINS.

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


def format_coin(price = 0, coin = '£'):
    return f'{coin} {price:.2f}'.replace('.', ',')