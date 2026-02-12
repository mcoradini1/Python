import random
#CHOOSE AN RANDOM NUMBER FROM A LIST
#I COULD USE: from random import choice, BUT I WOULD CHANGE BELLOW

n1 = str(input('Type the first student name: '))
n2 = str(input('Type the second student name: '))
n3 = str(input('Type the third student name: '))
n4 = str(input('Type the fourth student name: '))

list_students = [n1, n2, n3, n4]

chosen = random.choice(list_students)   #IT WOULD CHANGE TO: chosen = choice(lista)
print('The student that will present is {}'.format(chosen))