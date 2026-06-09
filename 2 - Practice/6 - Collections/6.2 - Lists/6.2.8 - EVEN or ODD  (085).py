# ======================================================================================================================
# CHALLENGE 85: EVEN or ODD (Composite lists): Read 7 numbers, tell EVEN or ODD and put them in order
# ======================================================================================================================

"""
Challenge: 6.2.8 - EVEN or ODD  (085)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - if()
    - else()
    - .sort()


Tags: list, .append(), if(), else(), .sort()
Status: ✔️ Completed
"""


# FIRST APPROACH =======================================================================================================

list_general = list ()
lista_even = list ()
lista_odd = list ()

for c in range (0,7):
    a = int(input(f'Type {c+1} number: '))
    if a % 2 == 0:
        lista_even.append(a)
        print('Even')
    else:
        lista_odd.append(a)
        print('Odd')
lista_even.sort()
lista_odd.sort()
list_general.append(lista_even[:])
list_general.append(lista_odd[:])


print(f'EVENS {list_general[0]} \nODDS {list_general[1]}')

# SECOND APPROACH ======================================================================================================

list_general = [[], []]

for c in range (1,8):
    a = int(input(f'Type {c} number '))
    if a % 2 == 0:
        list_general[0].append(a)
    else:
        list_general[1].append(a)

list_general[0].sort()
list_general[1].sort()

print(f'EVENS {list_general[0]} \nODDS {list_general[1]}')