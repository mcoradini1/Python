# ======================================================================================================================
# CHALLENGE 87: MATRIX IMPROVED (total of evens, sum of third column, higher value on second line)
# ======================================================================================================================

"""
Challenge: 6.2.10 - MATRIX IMPROVED  (087)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - for
    - range
    - end = ''
    - if()


Tags: list, .append(), for, range, end = '', if()
Status: ✔️ Completed
"""


matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even_sum = 0
column_3 = 0
higher_2 = 0

for lines in range (0, 3):
    for columns in range (0, 3):
        matrix[lines][columns] = int(input(f'Type a value for: [{lines}, {columns}] '))
print('=-'*60)

for lines in range (0, 3):
    for columns in range(0, 3):
        if matrix[lines][columns] % 2 == 0:
            even_sum = even_sum + matrix[lines][columns]

for lines in range (0, 3):
    column_3 = column_3 + matrix[lines][2]

for columns in range (0, 3):
    if matrix[1][columns] > higher_2:
        higher_2 = matrix[1][columns]

for lines in range (0, 3):
    for columns in range(0, 3):
        print(f'[{matrix[lines][columns]:^5}]', end =' ')
    print()

print(f'The total sum of EVENS is {even_sum}\nThe sum of the third column is {column_3}'
      f'\nThe higher value in second line is {higher_2} ')

