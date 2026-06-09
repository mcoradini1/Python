"""
---------------------------------- STRINGS IMMUTABLE -------------------------------------------------------------------
Strings are immutable so to use the functions bellow it is important to use another variable if we have plans to use
the variable. If the plan is just to print the variable it can be done inside, but the variable will not change.

a = 'Hello World'
print(a.upper())     -  All upper here (don't change a)
print(a)             -  Variable still the same
b = a.upper()
print(b)             -  Now b has the value of 'a' all upper

------------------------------------ .split() --------------------------------------------------------------------------
Divide the variable phrase into a list where spaces determine each element
To show elements from lists in front of the variable we add [0,1,2...] decide the which element of the
list to see as 0 is the first term of the list

ps: LISTS are collective elements to learn more go to COLLECTIONS.

----------------------------------- .join() ----------------------------------------------------------------------------
Join the list, in the case bellow using - as space.

---------------------------------- .strip() ----------------------------------------------------------------------------
Cuts spaces on the beginning and ending of variables

---------------------------------- .upper() and .lower() ---------------------------------------------------------------
Set letters to CAPITALIZE, LOWERCASE
    .upper()[0] In this case I am making the first letter as capital

------------------------------------ .len() ----------------------------------------------------------------------------
Counts the size of characters of the variable, considering even the invisible spaces.

---------------------------------- .count('x') -------------------------------------------------------------------------
Count the number of characters of the variable, considering even the invisible spaces. (Case sensitive)
    It is good to work this with .lower or .upper

---------------------------------- .replace('old','new') ---------------------------------------------------------------
Replace text

---------------------------------- .find('word') -----------------------------------------------------------------------
It will tell exactly where it will find the word first time. If returns -1 this means it could not find the word

    It is good to work this with .lower or .upper
    To make the command works right to left we just add an 'r' in front of the command

    Examples:
    print('Test {}'.format(variable.find('A')+1))
    print('Test {}'.format(variable.rfind('A')+1))

---------------------------------- .index() ----------------------------------------------------------------------------
Show the index of the number.

---------------------------------- Stings works like LISTS -------------------------------------------------------------
'Strings are considered as a list of letters' with that in ind we can work SLICING techniques 5.1 - For STRINGS

------------------------------------------ SLICING ---------------------------------------------------------------------
'Strings are considered as a list of letters' with that in ind we can work SLICING techniques 5.1 - For STRINGS

    phrase[start:end:step]:

    phrase[3] Get only the third element in this case 'T'
    phrase[3:13] Get the 3rd element until the 13th (not considering 13th)
    phrase[::2] Without start. Without ending, going 2 by 2

------------------------------------------ POLYMORPHISM ----------------------------------------------------------------
This is a function in python that sum/multiply 'words'

b = 'hello' + 'world' (will result helloworld)

s = 'python'
3*s PythoPythonPython



------------------------------------------ ''' LONG TEXTS ''' ----------------------------------------------------------
print('''

All text here will follow
line 1
line 2
line 3

''')

"""

phrase = '01 - Python as a programming Language  '

divided = phrase.split()

join = '-'.join(divided)
strip = phrase.strip()
capitalize = phrase.upper()
replace = phrase.replace('01 - Python', 'Android')

print('FIRST COMMANDS')
print(f'Normal: {phrase} it has {len(phrase)} characters')
print(f'Join (-): {join} it has {len(join)} characters')
print(f'Strip: {strip} it has {len(strip)} characters')
print(f'Capitalize: {capitalize}')
print(f'Counting efficient "o": ',phrase.upper().count('O'))
print(f'Replace: {replace} it has {len(replace)} characters')
print('The word language appears in ', phrase.lower().find('language'))


print('\n')
print('AS LIST COMMANDS')
print(f'As a LIST: {divided}')
print(f'As a LIST by element (first element): {divided[0]}')
print(f'As a LIST by element (second element): {divided[1]}')

print('\n')
print('SLICING')
print(phrase[3])
print(phrase[3:13])
print(phrase[::2])


