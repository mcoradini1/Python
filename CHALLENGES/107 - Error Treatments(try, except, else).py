#A PROGRAM TO CHECK IF A NUMBER IS A INT

def isint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Entrance is not valid')
            continue
        except KeyboardInterrupt:
            print('User decide to terminate the program')
            return 0
        else:
            return n

n1 = isint('Type a number: ')
print(n1)