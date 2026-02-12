#PROGRAM TO READ A NUMBER AND DECIDE BETWEEN ODD AND EVEN
num = int(input('Type a number: '))
check = num % 2
if check==0:
    print('The number {} is even'.format(num))
else:
    print('The number {} is odd'.format(num))