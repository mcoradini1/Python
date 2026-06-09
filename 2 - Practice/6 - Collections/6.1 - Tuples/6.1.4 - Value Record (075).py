# ======================================================================================================================
# CHALLENGE 75: Value Record: Input 4 numbers then count how many 9 is typed, which position is three and EVEN values
# ======================================================================================================================

"""
Challenge: 6.1.4 - Value Record (075)
Category: 6 - Collections
Concepts Used:
    - tuples
    - if()
    - else()
    - for
    - .index()
    - end = ''


Tags: tuples, if(), else(), for, .index(), end = ''
Status: ✔️ Completed
"""

i = (int(input('Type a number: ')),
     int(input('Type another number: ')),
     int(input('Type another number: ')),
     int(input('Type another number: ')))

print(i)
print(f'-> The number 9 appeared {i.count(9)}')
if 3 in i:
    print(f'-> The number three appeared the first time at {i.index(3)+1} positon')
else:
    print('-> The number three did not appear at all')
print('-> The pair numbers are: ')

for n in i:
    if n % 2 == 0:
        print(n, end = ' ')


