#No limits in here...
#while something dont happen I will continue the repetition
#Structure of repetiton with logical test

apple = 0
while not apple == 20:
    print('We still don`t have enough {}'.format(apple))
    apple+=1

while apple < 20:
    print('That`s another way o do it...\n\n\n')

n = 1
even = odd = 0
while n != 0:
    n=int(input('Type a value (0 closes): '))
    if n != 0:
        if n%2 == 0:
            even += 1
        else:
            odd += 1
print('evens: {}\nodds: {}'.format(even,odd))

