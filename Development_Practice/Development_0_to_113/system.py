from lib.interface import *
from lib.archive import *
from time import sleep
from sys import exit

archive_txt = 'system.txt'

if not archive_txt_exists (archive_txt):
    generate_archive(archive_txt)

while True:
    answer = menu(['Check Registration List','Register New Person','Exit'])
    if answer == 1:    #LIST CONTENT INSIDE
        read_archive(archive_txt)
        sleep(1)
    elif answer == 2: #NEW REGISTRATION
        ui_header('NEW REGISTRATION')
        name = str(input('Name: ')).strip()
        if name == '':
            name = '<unknown>'
        age = read_int('Age: ')
        add_to_archive(archive_txt,name,age)
        sleep(1)
    elif answer == 3: #QUIT
        print(f'{color(1)}SHUTTING DOWN!')
        sleep(1)
        print('Thank you for your time!')
        exit(0)
        break
    else:
        print(f'{color(1)}ERROR! Try again {color(0)}')
        sleep(1)

