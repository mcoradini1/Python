#LISTS INSIDE LIST
#WORK OF COMPOSITE LIST
from os.path import realpath

people = [['Peter', 25], ['Mary', 19], ['John', 32]]
#List people has Peter on term 0
#List Peter has 25 as term 0

#PRINTING --------------------------------------------------------------------------------------------------------------
print(people[0][0]) #PETER IS THE ANSWER (PETER LIST)
print(people[1][1]) #19 IS THE ANSWER (MARY LIST)
print(people[2][0]) #JOHN (JOHN LIST)
print(people[1]) #MARY AND 19 [Mary, 19]
#A BIT FURTHER WE ARE GOING TO USE DICTIONARIES TO CHANGE THE NUMBERS, BUT FOR NOW WE USE NUMBERS)


#WRONG WAY -------------------------------------------------------------------------------------------------------------
#DOING THIS WAY, I WILL BOND THE LIST PEOPLE1 TO LIST EVERYBODY
people1 = list ()
people1.append('Marlon')
people1.append('30')
everybody = list ()
everybody.append(people1) #HERE I SHOULD USE everybody.append(people1[:])

#HERE I AM CHANGING EVERYBODY/PEOPLE1 BECAUSE THEY ARE BONDED
people1[0] = 'Susana'
people1[1] = 28

print(everybody)
print(people1)
#BOTH WILL PRINT THE SAME VALUE [Susana, 28]


#FURTHER COMPREHENSION  ------------------------------------------------------------------------------------------------
everybody1 = [['John', 19], ['Marlon', 30], ['Susana', 28], ['Gabi', 19]]
print(everybody1) #EVERYTHING WILL BE SHOWN
print(everybody1[2][1]) # [28]


#USING FOR INSIDE LISTS ------------------------------------------------------------------------------------------------
for p in everybody1: #FOR EACH PERSON INSIDE THE LIST
    print(p) #SHOWS NAME AND AGE
    print(p[1]) #SHOW AGE OF EACH
    print(f'{p[0]} is {p[1]} years old')

#MANUAL LISTS EXAMPLE  -------------------------------------------------------------------------------------------------
everybody2 = list ()
database = list ()
for c in range (0,3): #DON'T CONSIDER 3)
    database.append(str(input('Name: ')))
    database.append(int(input('Age ')))
    everybody2.append(database[:]) #COPYING TO AVOID BOND BETWEEN THEM
    database.clear() #THIS CLEAR DATABASE, IN CASE IT'S BONDED TO EVERYBODY2, BOTH COULD BE DELETED
print(everybody2)

real_age = total_minor = 0 #SIMPLE VARIABLES, I CAN EQUAL THAN WITHOUT ISSUES OF BONDING
for p in everybody2:
    if p[1] >= 21:
        print(f'{p[0]} is legal age')
        real_age+=1
    else:
        print(f'{p[1]} is under age')
        total_minor+=1
print(f'The total legal age are {real_age} and minor age are {total_minor}')
