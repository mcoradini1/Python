#FUNCTIONS (def) brings functionalities to the user, as an example PRINT is a 'default function'
#They are great to facilitate things that we repeat a lot while programming.

#REMEMBER:
# 1 - I Always have parenthesis in front of functions
# 2 - Between def and the program I should leave 2 blank lines, otherwise the software will complain (organization)

#EXAMPLE 1 (basic without variables) -----------------------------------------------------------------------------------
def show_hyphen():
    print('---------------------------------------------------------')
    #SIMPLY FUNCTION THAT WILL PRINT A LINE WITH HYPHENS

show_hyphen()
print('MIAU')
show_hyphen()

#EXAMPLE 2 (using only one local variable msg) -------------------------------------------------------------------------
def message(msg):
    print('-'*60)
    print(msg)
    print('-'*60)

message('This will show the message between 2 lines of HYPHENS')

#EXAMPLE 3 (using 3 local [a,b and s] variables) -----------------------------------------------------------------------
def sum(a, b):
    s = a + b
    print(s)
    print(f' A soma A + B e igual a {s}')

sum (4, 5) #I CAN ONLY ADD THE NUMBERS,AND IT WILL CONSIDER A AND B (BY THE ORDER)
sum(8, 9)
sum(2, 1)

sum(a=5, b=10) #WRITING THE VARIABLE WORKS IN ANY ORDER
sum(b=2, a=3)

sum(a=3, 6) #DON'T WORK
sum(4) #DON'T WORK BECAUSE WE HAVE TWO VARIABLES TO BE CONSIDER

#UNKNOWN AMOUNT OF VARIABLES (PACKING PARAMETERS) ----------------------------------------------------------------------
#WHEN I DON'T KNOW HOW MANY NUMBERS, THIS IS A THING THAT PYTHON IS UNIQUE...
def counter1 (* num): #IT WILL PROVIDE THE AMOUNT OF VARIABLES THAT THE PROGRAM WILL NEED.
#IT WILL GENERATE A TUPLE TO STORE THE VARIABLES.

#EXAMPLE 4 (COUNTER) ---------------------------------------------------------------------------------------------------
def counter(*num):
    for valor in num:
        print(f'{valor}', end='')
    print('FIM!')


counter(2, 1, 4, 3)
counter(2, 3)
counter(8, 6, 0, 0, 0, 8, 4, 32)


#WORKING WITH LISTS (THIS IS NOT PACKING) ------------------------------------------------------------------------------
#EXAMPLE 5 THIS IS A FUNCTION TO TAKE A LIST AND MULTIPLY IT BY 2. -----------------------------------------------------

def twice(list):

    pos = 0
    while pos < len(list):
        list[pos]*=2
        pos +=1


values = [7, 8, 8, 5, 7, 89]
twice(values)
print(values)

#EXAMPLE 6 SUM THE NUMBERS ---------------------------------------------------------------------------------------------
def soma2(*values1):
    s = 0
    for num in values1:
        s+= num
        print(f'summing {num} we have {s}')