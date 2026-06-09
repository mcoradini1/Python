# ======================================================================================================================
# CHALLENGE 81: Infinite Reverse: with stop criteria from higher to lower, check if 5 is found within the list
# ======================================================================================================================

"""
Challenge: 6.2.4 - Infinite Reverse (081)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - if()
    - while
    - while True
    - break
    - .sort()
    - reverse = True
    - len()


Tags: list, .append(), if(), while, while True, break, .sort(), reverse = True, len()
Status: ✔️ Completed
"""

list_infinite = list ()
while True:
    list_infinite.append(int(input('Type a number: ')))
    r = str(input('Do you want to continue? Y/N'))
    if r in 'Nn':
        break
list_infinite.sort(reverse = True)
print(' - '*60)
print(f'[{len(list_infinite)}] Numbers typed\nThe values inside the list are: {list_infinite}')
if 5 in list_infinite:
    print('The value 5 was FOUND in the list')
else:
    print('The value 5 was NOT FOUND in the list')

