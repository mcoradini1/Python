# ======================================================================================================================
# CHALLENGE 78: Value Record: Receive 5 values, provide higher, lower and show position of each
# ======================================================================================================================

"""
Challenge: 6.2.1 - Value record (078)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - for
    - enumerate()
    - max()
    - min()
    - range


Tags: list, .append(), for, enumerate(), max(), min(), range
Status: ✔️ Completed
"""

# FIRST APPROACH =======================================================================================================

list_values = list()
for count in range(0, 5):
    list_values.append(int(input('Type a number: ')))
print('-'*60)
print(f'The highest is {max(list_values)} and appeared at position  {list_values.index(max(list_values))+1}')
print(f'The lower is {min(list_values)} and appeared at position  {list_values.index(min(list_values))+1}')
print('-'*60)
for c, c1 in enumerate(list_values):
    print(f'The term {c} is number {c1}')


# SECOND APPROACH ======================================================================================================

list_numbers = []
higher_number = 0
lower_number = 0
for c in range(0,5):
    list_numbers.append(int(input(f'Type a number for the position {c} ')))
    if c == 0:
        higher_number = lower_number = list_numbers[c]
    else:
        if higher_number < list_numbers[c]:
            higher_number = list_numbers[c]
        if lower_number > list_numbers[c]:
            lower_number = list_numbers[c]
print('-'*60)
print(f'The higher is {higher_number}, the lower is {lower_number}\n and the complete list is: {list_numbers}')
print('-'*60)

