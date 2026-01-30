#PREPARE A FUNCTION TO ADD LINES ABOVE AND BELLOW A TEXT, FOLLOWING THE SIMILAR SIZE OF THE TEXT

def write_line(name):
    a = len(name) + 2
    print('~'*a)
    print(f' {name}')
    print('~'*a)

write_line('Functions are cool')
write_line('Python is cool')
