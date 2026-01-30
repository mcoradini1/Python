#PROGRAM TO TYPE SCHOOL REPORT OF
# (A) ADD STUDENTS GRADES AND NAMES
# (B) SHOW THE INFORMATION

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
