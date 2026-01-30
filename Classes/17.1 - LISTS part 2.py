num = [2,5,9,1]
num.append(7) #ADD THE NUMBER 7 BY THE END [2,5,9,1 and 7]
num.sort() #ORGANISE IN ORDER CRESCENT
print(num)
num.insert(2,83) #ADD 83 ON POSITION 2 [1,2,>83<,5,7,9]
num.remove(2)
print(f'There are {len(num)} in the list\n\n')
print(num)

for v in num:    #IN THIS WAY I CAN GET THE NUMBERS FROM THE LIST
    print(f'{v}',  end = ' ')

for c, v in enumerate(num): #WITH ENUMERATE I CAN TAKE THE NUMBER AND POSITION
    print(f'{c} is my position\n {v} Is my number')

values = list() #ADD VALUES TO A LIST
for count in range(0, 5):
    values.append(int(input('Type a value: ')))

#PECULIARITIES IN PYTON ------------------------------------------------------------------------------------------------
# IF I EQUAL TWO LISTS, THEY WILL HAVE AN BOND FOR THE WHOLE PROGRAM
a = [2,3,4,7]
b = a
b[2] = 8 # CHANGING THE TERM 2 OF LIST 2, BUT AS A AND B HAS AN BOND, BOTH WILL BE CHANGED
print(a,b) #HERE I CAN SEE THAT BOTH LISTS ARE [2,3,8,7]


#COPYING LIST ----------------------------------------------------------------------------------------------------------
b = a[:] #THIS WY I CAN GET ALL ELEMENTS FROM LIST A (NOT CREATING A BOND BETWEEN THEM)
#IN CASE OF CHANGE, A AND B ARE NOT BONDED.
