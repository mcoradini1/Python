# ======================================================================================================================
# CHALLENGE 56: Name,Age,Sex: Read these from 3 people and returns the average age, older man, and women younger than 20
# ======================================================================================================================

"""
Challenge: 5.1.11 - Name,Age,Sex (056)
Category: 5 - Loops
Concepts Used:
    - for
    - range()
    - if()
    - and
    - else()


Tags: for, range(), if(), and, else()
Status: ✔️ Completed
"""

age_average = 0
old = 0
name_old = 0
women_20 = 0 #WOMEN LOWER 20
for c in range (1,4):
    name = str(input('The name of the {} participant '.format(c)))
    age = int(input('The age of the {} participant '.format(c)))
    sex = int(input('What is the sex of the {} participant \n[1] Male\n[2] Female\n'.format(c)))
    age_average+= age
    if sex == 2 and age<20:
        women_20+=1
    if age > old and sex == 1:
        old = age
        name_old = name
if old == 0:
    print('The average age is {}\nThere is no man in this group\nWe have {} with lower 20 years old '
          .format(age_average / 2, name_old, old, women_20))
else:
    print('The average age is {}\nThe older man name is {} and he is {} years old\nWe have {} with lower 20 years old '
          .format(age_average / 2, name_old, old, women_20))