def line(size = 60):
    return '-' * size

def ui_header(txt):
    print(line())
    print(txt.center(60))
    print(line())

def read_int(msg): #FROM PRACTICE 104.
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

def color(color_number): #FROM PRACTICE 106

    list_color = [
    '\033[m',        #0 - no color
    '\033[31m',      #1 - red
    '\033[32m',      #2 - green
    '\033[33m',      #3 - yellow
    '\033[34m',      #4  - blue
    '\033[35m',      #5 - purple
    '\033[7m',       #6 - white
    ]

    return list_color[color_number]

def menu(list_menu):
    ui_header(f'{color(6)}-- PRINCIPAL MENU --{color(0)}')
    c = 1
    for item in list_menu:
        print(f'{color(5)}{c}{color(0)} - {color(4)}{item}{color(0)}')
        c += 1
    print(line())
    opt = read_int(f'{color(2)}Select an option: {color(0)}')
    return opt

