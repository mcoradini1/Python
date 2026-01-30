#CREATE A FUNCTION TO VALIDATE A INTEGER VARIABLE.

def read_int(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0;31mERROR, Try again!\033[m ')
        if ok:
            break
    return value

number = read_int('Type a number: ')
print(f'You typed {number}')


