#A PROGRAM TO CHECK IF 3 LINE SEGMENTS CAN GENERATE A TRIANGLE

print('-='*20)
print('        Triangle Analyzer 2000')
print('-='*20)
l1 = float(input('\nType the first number: '))
l2 = float(input('Type the second number: '))
l3 = float(input('Type the third number: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('These three segments CAN generate a triangle.')
else:
    print('The three segments CANNOT generate a triangle.')