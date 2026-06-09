# ==========================================================================================================
# CHALLENGE 20: SHUFFLE VARIABLES IN A LIST
# ==========================================================================================================

"""
Challenge: 3.5 - Random Shuffle (020)
Category: 3 - Numbers, Math and Logic
Concepts Used:
    - float()
    - .format()
    - input()
    - import random
    - shuffle()


Tags: float(),input(),.format(), random, shuffle()
Status: ✔️ Completed
"""

import random #COULD BE: from random import shuffle
n1 = str(input('Enter the name of the first student: '))
n2 = str(input('Enter the name of the second student: '))
n3 = str(input('Enter the name of the third student: '))
n4 = str(input('Enter the name of the fourth student: '))

list_students = [n1, n2, n3, n4]
print('The original list of the students is {}'.format(list_students))
random.shuffle(list_students) #WOULD BE ONLY shuffle(list_students)
print('The shuffled list is {} '.format(list_students))

