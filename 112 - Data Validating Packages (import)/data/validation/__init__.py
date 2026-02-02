#FUNCTION TO VALIDATE
def validate_num(msg):
    is_num_valid = False
    while not is_num_valid:

        check = str(input(msg)).replace(',', '.').strip()
        if check.isalpha() or check == '':
            print(f'\033[30;41m ERROR! \"{check}\" is NOT valid.\033[m')

        else:
            is_num_valid = True
            return float(check)
    return None






