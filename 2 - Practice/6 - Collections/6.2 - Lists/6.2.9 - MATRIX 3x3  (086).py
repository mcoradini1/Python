# ======================================================================================================================
# CHALLENGE 86: MATRIX 3x3
# ======================================================================================================================

"""
Challenge: 6.2.9 - MATRIX 3x3  (086)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - for
    - range
    - end = ''


Tags: list, .append(), if(), else(), .sort()
Status: ✔️ Completed
"""


# FIRST APPROACH =======================================================================================================

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lines in range (0, 3):
    for columns in range (0, 3):
        matrix[lines][columns] = int(input(f'Type a value for: [{lines}, {columns}] '))
print('=-'*60)

for lines in range (0, 3):
    for columns in range(0, 3):
        print(f'[{matrix[lines][columns]:^5}]', end =' ')
    print()


