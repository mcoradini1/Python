# ==========================================================================================================
# CHALLENGE 19: CHOOSE AN RANDOM VARIABLE FROM A LIST
# ==========================================================================================================

"""
Challenge: 3.4 - Random Choice (019)
Category: 3 - Numbers, Math and Logic
Concepts Used:
    - float()
    - .format()
    - input()
    - import random
    - choice()


Tags: float(),input(),.format(), random, choice()
Status: ✔️ Completed
"""

import random

n1 = str(input('Type the first student name: '))
n2 = str(input('Type the second student name: '))
n3 = str(input('Type the third student name: '))
n4 = str(input('Type the fourth student name: '))

list_students = [n1, n2, n3, n4]

chosen = random.choice(list_students)
print('The student that will present is {}'.format(chosen))