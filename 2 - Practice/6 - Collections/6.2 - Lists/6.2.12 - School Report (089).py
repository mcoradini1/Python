# ======================================================================================================================
# CHALLENGE 89: School Report: (A) add students grades and names, and (B) show information
# ======================================================================================================================

"""
Challenge: 6.2.12 - School Report (089)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - while
    - while True
    - not in
    - in
    - break
    - range
    - for
    - range
    - len()

Tags: list, .append(), while, while True, not in, in, break, range, for, range, len()
Status: ✔️ Completed
"""


#FIRST APPROACH ========================================================================================================
school_report = [[], []]
students = list ()
grade = list()

while True:
    print('-'*60)
    students.append(str(input('Name: ')))
    grade.append(float(input('Test 1: ')))
    grade.append(float(input('Test 2: ')))
    print('-'*60)
    r = str(input('Do you want to add another student? Y/N '))
    while r not in 'YyNn':
        r = str(input('Do you want to add another student? Y/N '))
    if r in 'Nn':
        break
school_report[0].append(students[:])
school_report[1].append(grade[:])

for n in range (0, len((school_report[1]))):

    print('n')


#SECOND APPROACH =======================================================================================================

school_report = list()

while True:
    name = str(input('Name: '))
    score_1 = float(input('Nota 1: '))
    score_2 = float(input('Nota 2: '))
    average = (score_1 + score_2) / 2
    school_report.append([name, [score_1, score_2], average])
    r = str(input('Do you want to add another student? Y/N '))
    while r not in 'nNyY':
        r = str(input('Do you want to add another student? Y/N '))
    else:
        if r in 'Nn':
            break

print('-'*60)
print(f'{'Number':<14}{'Name':<14}{'Average':<14}')
print('-'*60)
for i, i1 in enumerate(school_report):
    print(f'{i:<14}{i1[0]:<14}{i1[2]:<14}')
print('-'*60)

while True:
    v=int(input('Which student would you like to see the test scores? (999 closes): '))
    if v == 999:
        break
    if v <= len(school_report) - 1:
        print(f'As notas de {school_report[v][0]} sao {school_report[v][1]}')

print('PROGRAM CLOSED')
print('-'*60)