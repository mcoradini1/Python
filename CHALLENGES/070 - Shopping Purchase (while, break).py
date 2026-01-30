#A PROGRAM THAT WILL SIMULATE A PURCHASE, ENTERING THE NAME AND PRICE OF A PRODUCT AND RETURN:
#TOTAL PRICE, PRODUCTS ABOVE 1000£, AND CHEAPER PRODUCT
total = 0
above_1000 = 0
cheaper_product = ''
cheaper_value = 0
while True:
    print('-'*60)
    product_name = str(input('What is the name of the product: ')).strip().title()
    product_price = float(input('Product price: '))
    print('-'*60)
    total = total + product_price
    if product_price >= 1000:
        above_1000+=1
    if cheaper_value == 0:
        cheaper_value = product_price
        cheaper_product = product_name
    if cheaper_value > product_price:
        cheaper_value = product_price
        cheaper_product = product_name

    more_product = str(input('Do you want to add another product? (Y/N) ')).strip().upper()
    while True:
        if more_product == 'Y' or 'N':
            break
    if more_product == 'N':
        break

print('-'*60)
print(f'\n\nThe total value is {total:.2f}£\n{above_1000} Product(s) over 1000,00£\n{cheaper_product} is the cheaper product priced {cheaper_value:.2f}£')
print('-'*60)