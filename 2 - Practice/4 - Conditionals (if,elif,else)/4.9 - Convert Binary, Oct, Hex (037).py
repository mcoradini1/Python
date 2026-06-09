# ====================================================================================================================
# CHALLENGE 37: Convert Binary, Oct, Hex: Read a number and convert it to Binary/Octal/Hexadecimal
# ====================================================================================================================

"""
Challenge: 4.9 - Convert Binary, Oct, Hex (037)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - int()
    - if()
    - elif()
    - else()
    - bin()
    - oct()
    - hex()
    - .format
    - print()


Tags: int(), if(), elif(), else(),bin() ,oct() ,hex() , .format, print()
Status: ✔️ Completed
"""


num = int(input('Type a number: '))
base = int(input('''5.1 - For each base it will be converted ? 
[1] Binary
[2] Octal
[3] Hexadecimal 
-> '''))
if base == 1:
    print('The value in BINARY -> {}'.format(bin(num)))
    print('The value in BINARY -> {}'.format(bin(num)[2:])) #[2:] This slicing is just to cut the 0B (default in front every binary)
elif base == 2:
    print('The value in OCT -> {}'.format(oct(num)))
    print('The value in OCT -> {}'.format(oct(num)[2:]))
elif base == 3:
    print('The value in HEXADECIMAL-> {}'.format(hex(num)))
    print('The value in HEXADECIMAL-> {}'.format(hex(num)[2:]))
else:
    print('Number not identified')
