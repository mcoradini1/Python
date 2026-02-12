#READ WIDTH AND HEIGHT OF AN WALL, AND CALCULATE AMOUNT OF PAINT. (1 PAINT CAN = 2 m2)
w = float(input('Enter the wall width: '))
h = float(input('Enter the wall height: '))


print('The wall has {} m2'.format(w*h))
print('To paint this wall will be necessary {:.0f} paint cans'.format(w*h/2))
