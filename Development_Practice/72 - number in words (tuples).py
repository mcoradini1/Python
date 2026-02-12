#A PROGRAM TO RECEIVE A NUMBER FROM 0 TO 20 AND RETURN THE NUMBER WROTE DOWN

tup = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
       'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    i = int(input('Type a number from 0 to 20: '))
    if 0 <= i <= 20:
        break
    print('Try again, ', end = '')

print(f'You typed the number {tup[i]}')