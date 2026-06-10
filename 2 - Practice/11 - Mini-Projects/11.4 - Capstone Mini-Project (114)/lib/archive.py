def archive_txt_exists(name):
    try:
        a = open(name, 'rt')          #command to open an archive, and 'rt' means READ and TEXT.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def generate_archive(name):
    try:
        a = open(name, 'wt+')  # 'wt+' WRITE and TEXT, + will create in case does not exist
        a.close()
    except:
        print('There is a problem with the file')
    else:
        print(f'{color(3)}Archive {name} generated successfully!{color(0)}')


def read_archive(name):
    try:
        a = open(name, 'rt') #read text archive again.
    except:
        print('There is a problem with the file')
    else:
        ui_header('REGISTERED PEOPLE')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n','')
            print(f'{data[0]:<30}{data[1]:>3} years old')


        #print(a.read())               #command read 5.1 - For a simple read... can also use readlines() it will add even \n

    finally:
        a.close()


def add_to_archive(archive_name,name_person = '<unknown>',age_person = 0):
    try:
        a = open(archive_name, 'at')  #'at' APPEND TEXT, it will append
    except:
        print('There is a problem with the file')
    else:
        try:
            a.write(f'{name_person};{age_person}\n')
        except:
            print('There was a problem adding the information to the archive')
        else:
            print(f'New registration {name_person} and {age_person} are added to the archive')
            a.close()


# ------------------------------- INTERFACE

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

def color(color_number):

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

color(3)
print('erewr')