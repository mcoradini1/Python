"""
---------------------------------- .FORMAT -----------------------------------------------------------------------------
Will fill the specific location marked as {} with the variable in left to right order
    print('{}{}).format(variable1,variable2...)

-------------------------------------------- F STRINGS -----------------------------------------------------------------
Similar to .format, but inside the {} we have to fill the variable. Just need to add f before the '
    print(f'{variable1}...')

----------------------------------------------- END --------------------------------------------------------------------
END command will put the down line in front of the up line, everything inside it will be used instead of a paragraph.
    end=' >>> ' will add 3 right arrows instead of paragraph

----------------------------------- FORMATTING NUMBERS IN VARIABLES ----------------------------------------------------
-  {:.3f} To consider 3 variables after comma.
-  {:-^20} Add 20 - and center the variable
-  \n to break the line

"""

n1 = int(input('Type a value : '))
n2 = int(input('Type another value : '))
m = n1/n2

print('\nThe division: {:.3f}' .format(m), end=' >>> ')
print('{} / {}'.format(n1, n2))

name = 'Jose'
age = 33
salary = 1256.365484

#USING F STRING
print('------ Here some different text format ------\n')
print(f'{name} is {age} and his salary is {salary:.2f}\n') #.2f to consider only 2 decimals after the comma
print(f'{name:-^20}') #Centered in the middle of 20 ^
print(f'{name:20}') #20 invisible spaces in front
print(f'{name:^20}') #20 invisible spaces but centered
print(f'{name:-<20}') #20 instead of spaces hifen
print(f'{name:->20}') #20 instead of spaces hifen

#USING FORMAT
print('Nice to meet you {:-^20}'.format(name)) #one example using .format

