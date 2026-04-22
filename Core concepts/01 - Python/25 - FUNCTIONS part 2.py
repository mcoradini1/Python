#INTERATCITVE HELP -----------------------------------------------------------------------------------------------------
#THIS WILL ALLOW US TO SEE THE DOCSTRINGS THAT HAVE THE INFORMATION ABOUT THE FUNCTION
#I CAN MAKE THOSE FOR THE FUNCTIONS THAT I PROGRAM

help(print)
help(input)
print(input.__doc__)

#OPTIONAL ARGUMENTS ----------------------------------------------------------------------------------------------------
#WE SET THE VARIABLES AS 0, THE FUNCTION WILL WORK EVEN IF WE DON'T ATTRIBUTE VALUE TO IT

def function(a=0,b=0,c=0):
    print(a)

function(a=1,b=0,c=0)


#SCOPE OF VARIABLES (GLOBAL AND LOCAL) ---------------------------------------------------------------------------------
#WE HAVE LOCAL (INSIDE THE FUNCTION) AND GLOBAL (WHOLE PROGRAM) VARIABLES.
#I CAN HAVE VARIABLES WITH SAME NAME LOCAL/GLOBAL
#INNSIDE A FUNCTION TO CONSIDER A GLOBAL VARIABLE, I HAVE TO ADD (GLOBAL)

y = 3 #GLOBAL
global_x = 8

def variables():
    global global_x #THIS MAKES global_x GLOBAL
    global_x = 9 #CHANGING THE GLOBAL VARIABLE
    x = 3
    y = 4 #LOCAL

    print(f'Variable {global_x} is GLOBAL')
    print(f'Variable {x} is LOCAL')
    print(f'Variable {y} is LOCAL') #That will not work...


print(x) #DOES NOT WORK BECAUSE IT IS LOCAL VARIABLE... ONY WORKS INSIDE THE FUNCTION
print(y) #WORKS BECAUSE IT IS A GLOBAL VARIABLE


#RETURNING VALUES (RETURN) ---------------------------------------------------------------------------------------------
#THE VALUE WILL BE RETURNED AND CAN BE USED OUTSIDE THE FUNCTION

def sum_no_return(a=0, b=0, c=0):
    s = a+b+c
    print(f'The sum is {s}')

sum_no_return(1, 5, 4)
sum_no_return(2, 2)
sum_no_return(6)


#USING RETURN ----------------------------------------------------------------------------------------------------------
def sum_with_return (a=0,b=0):
    s = a+b
    return s

#IN THIS WAY THESE VARIABLE R1 AND R2 WILL HAVE THE VALUE OF THE SUM (S)

r1 = sum_with_return(2,3)
r2 = sum_with_return(3,5)

#EXAMPLE 1 -------------------------------------------------------------------------------------------------------------

def factorial(number=1):
    f = 1
    for c in range(number, 0, -1):
        f *= c
    return f

f1 = factorial(1)
f2 = factorial(5)

print(f1, f2)


#EXAMPLE 2 -------------------------------------------------------------------------------------------------------------

def even_or_odd(a=0):
    if a % 2 ==0:
        return True
    else:
        return False

n = int(input('Type a number: '))

if even_or_odd(n):
    print('Even')
else:
    print('Odd')
