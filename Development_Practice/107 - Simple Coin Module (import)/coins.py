#MAKE A FUNCTION THAT INCREASES, DECREASE A VALUE (BY A RATE) AND FUNCTIONS TO *2 AND /2, AND USE IT AS IMPORT
#LIBRARIES ON TEST.

def increase(price, tax):
    return price + (tax*price/100)
def decrease(price, tax):
    return price + (tax * price / 100)
def twice(price):
    return price * 2
def half(price):
    return price / 2
