# ======================================================================================================================
# CHALLENGE 82: Infinite EVEN or ODD
# ======================================================================================================================

"""
Challenge: 6.2.5 - Infinite EVEN or ODD (082)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - if()
    - else()
    - for()
    - range


Tags: list, .append(), if(), else(), for(), range
Status: ✔️ Completed
"""


list_all = list ()
list_even = list ()
list_odd = list()
n = int(input('How many numbers do you want to add: '))
for c in range (0,n):
    list_all.append(int(input(f'Type the {c+1} number: ')))
for c1 in list_all:
    if c1 % 2 == 0:
        list_even.append(c1)
    else:
        list_odd.append(c1)

print(f'-> Even {list_even}\n-> Odd {list_odd}')

