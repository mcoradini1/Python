#PROGRAM TO CHECK TYPE OF TRIANGLE: EQUILATERAL, SCALENE OU ISOSCELES,
r1 = float(input('Type the first side of the triangle: '))
r2 = float(input('Type the second side of the triangle: '))
r3 = float(input('Type the third side of the triangle: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('These segments CAN generate a triangle', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERAL (all sides are equal).')
    elif r1 != r2 != r3:
        print('SCALENE (all sides different).')
    else:
        print('ISOSCELES (two sides are equal). ')

else:
    print('These segments CANNOT generate a triangle', end=' ')