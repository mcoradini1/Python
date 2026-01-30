#A PROGRAM TO READ 9 NUMBERS AND ADD THEM TO A 3X3 MATRIX.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lines in range (0, 3):
    for columns in range (0, 3):
        matrix[lines][columns] = int(input(f'Type a value for: [{lines}, {columns}] '))
print('=-'*60)

for lines in range (0, 3):
    for columns in range(0, 3):
        print(f'[{matrix[lines][columns]:^5}]', end =' ')
    print()


