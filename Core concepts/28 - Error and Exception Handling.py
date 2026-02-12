'''
There are a lot of different types of errors, syntatics, semantics

exception (treat them easily)

try: After this we try our expression.

except: This will happen in case there is an error, I can add specific errors or leave it as generic. I can have it for
how many cases I need.

except ValueError:
except type_error:
except KeyboardInterrupt:

else(optional): what will happen if it goes well.

finally(optional): Something that will happen in case it goes well or not.

'''

#FIRST EXAMPLE-----------------------------------------------------------------------------------------------------------

try:
    a = 10
    b = 0                  #We cannot divide anything by 0.
    c = a / b
except: #generic type of error.
    print('(EXAMPLE 1) Something went wrong.')
else:
    print('We are good')
finally:
    print('(EXAMPLE 1) Bye bye\n')

#SECOND EXAMPLE---------------------------------------------------------------------------------------------------------
#I CAN DO LIKE THAT TO FIND THE SPECIFIC ERROR AND MAKE IT MORE SOPHISTICATED LIKE NEXT EXAMPLE

try:
    a = 10
    b = 0
    c = a / b
except Exception as error:
    print(f'(EXAMPLE 2) 1 - Something went wrong. the error is {error}')
    print(f'(EXAMPLE 2) 2 - Something went wrong. the error is {error.__class__}')
else:
    print('We are good')
finally:
    print('(EXAMPLE 2) Bye bye\n')

#THIRD EXAMPLE----------------------------------------------------------------------------------------------------------
#THIS IS MORE TAILORED FOR THE ISSUE

try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
   print('(EXAMPLE 3) We cannot divide by zero')
else:
    print('We are good')
finally:
    print('(EXAMPLE 3) Bye bye\n\n')

#FOURTH EXAMPLE---------------------------------------------------------------------------------------------------------
#MORE TAILORED MODEL, ALSO CONSIDERING VALUE ERRORS, SHOWING THAT I CAN ADD HOW MANY EXCEPTS I WOULD LIKE.
try:
    a = int(input('Type first number: '))
    b = int(input('Type second number: '))
    c = a / b
except ZeroDivisionError:
   print('(ZeroDivisionError) We cannot divide by zero')
except ValueError:
   print('(ValueError) We can only use integer numbers.')
except TypeError:
    print('(TypeError) There is an typing error.')
except KeyboardInterrupt:
    print('\n(KeyboardInterrupt) User prefer to close the system')
else:
    print('We are good')
finally:
    print('(EXAMPLE 4) Bye bye')