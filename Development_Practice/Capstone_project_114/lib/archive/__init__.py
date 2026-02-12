from Development_Practice.Capstone_project_114.lib.interface import color
from Development_Practice.Capstone_project_114.lib.interface import ui_header


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


        #print(a.read())               #command read for a simple read... can also use readlines() it will add even \n

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

