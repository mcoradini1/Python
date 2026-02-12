#ALGORITHM TO READ A PRICE AND GIVE 5%, 10% and 15% DISCOUNT
p = float(input('What is the value of the product? ' ))
print('\nThis product is {} with 5%\nWith 10% {}\nWith 15% {}'.format(p*0.95,p*0.9,p*0.85))