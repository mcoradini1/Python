#IMPROVE THE PROGRAM 061, GIVING THE OPTION TO ADD EXTRA NUMBERS TO THE SEQUENCE:
t = int(input('Enter the first term '))
r = int(input('Enter the ratio '))
result = t
term_10th=0
while not term_10th == 11:
    print(result, end=' -> ')
    term_10th+=1
    result = result + r

t_extra = 1
t_extra_count = 0
while t_extra != 0:
    t_extra = int(input('END\n\nHow many extra terms would you like? '))
    t_extra_count = 0
    while not t_extra_count == t_extra:
        t_extra_count+=1
        result = result + r
        print(result, end =' -> ')

print('\nSHUTTING THE SYSTEM DOWN')
