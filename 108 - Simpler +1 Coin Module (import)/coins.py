#IMPROVE THE EXERCISE 107, BY A NEW FUNCTION THAT WILL FORMAT THE TEXT, AND CHANGE DOTS BY COMMAS.

def increase(price = 0, tax = 0):
    return price + (tax*price/100)


def decrease(price = 0, tax = 0):
    return price + (tax * price / 100)


def twice(price = 0):
    return price * 2


def half(price = 0):
    return price / 2


def format_coin(price = 0, coin = '£'):
    return f'{coin} {price:.2f}'.replace('.', ',')