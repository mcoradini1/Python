#LISTS are changeable, they are similar to TUPLAS (but changeable)
#LISTS have different commands
#[] <- Determine LISTS


#ADD -------------------------------------------------------------------------------------------------------------------
list0 = []
list1 = list ()
animals = ['bull', 'cow', 'lion']
animals[2] = 'armadillo' #THIS CHANGES LION AND ADDS ARMADILLO
animals.append('anteater') #THIS ADD TO THE END ANTEATER (Term number 3)
animals.insert(0, 'calf') #THIS ADDS CALF AS TERM NUMBER 0, MOVING EVERYTHING TO FRONT...


#DELETE ----------------------------------------------------------------------------------------------------------------
del animals [3] #DELETE
animals.pop(3) #NORMALLY USED TO DELETE THE LAST TERM, BUT I CAN ADD INDEX HERE (THIS WILL DELETE THE 3 TERM)
animals.pop() #DELETE THE LAST
animals.remove('bull') #DELETE THIS SPECIFIC TERM IN THE LIST
#IT WILL DELETE AND REORGANIZE EVERYTHING


#DELETE TIPS -----------------------------------------------------------------------------------------------------------
if 'cow' in animals: #IF I ASK TO DELETE SOMETHING THAT IS NOT IN THE LIST, THE PROGRAM WILL BREAK
    animals.remove('boi')


#USING RANGE -----------------------------------------------------------------------------------------------------------
#I ALREADY USED RANGE BEFORE, IT START ON 4 AND GO UNTIL 11 (NOT CONSIDERING 11)
values = list(range(4,11))
#A LIST WITH THE ELEMENTS (456789 AND 10)

#ORGANISING VALUES -----------------------------------------------------------------------------------------------------
out_order_values = [1, 4, 5, 6, 9, 34, 9, 2]
out_order_values.sort() #PUT THEM IN ORDER (CRESCENT)
out_order_values.sort(reverse=True) #PUT THEM IN ORDER (DECRESCENT)
len(out_order_values) #SHOW ME THE SIZE OF THE LIST


#INDEX (IT WILL SHOW ME IN WHICH POSITION IS THE FIRST 9) --------------------------------------------------------------
out_order_values.index(9)







