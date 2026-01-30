#PREPARE A SIMPLE FUNCTION TO CALCULATE AREA USING LENGTH AND WIDTH.

def area(length, width):
    area_func = length * width
    print(area_func)

length_real = float(input('Type the length: '))
width_real = float(input('Type the width: '))
area(length_real, width_real)


print()
area(3,2)



