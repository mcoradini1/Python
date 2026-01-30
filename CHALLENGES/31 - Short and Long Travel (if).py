#MAKE A PROGRAM TO CALCULATE PRICES OF BUS TRAVEL, CONSIDERING
#SHORT DISTANCE (< 200 MILES) - 0.50£/miles
#LONG DISTANCES (+ 200) - 0.45£/miles

distance = float(input('Type the travel distance: '))
if distance <= 200:
    price = distance * 0.50
    print('Your travel will be {:.2f}£'.format(price))
else:
    price = distance * 0.45
    print('Your travel will be {:.2f}£'.format(price))

