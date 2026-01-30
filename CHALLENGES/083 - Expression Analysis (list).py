#A PROGRAM TO READ/ANALYSE EXPRESSIONS AND TELL IF EVERYTHING IS ALRIGHT (SPECIFICALLY PARENTHESIS)
expression = str(input('Type the expression: '))
parenthesis = []
for paren in expression:
    if paren == '(':
        parenthesis.append('(')
    elif paren == ')':
        if len(expression) > 0:
            parenthesis.pop()
        else:
            parenthesis.append(')')
print(f' -> {parenthesis}')

if len(parenthesis) == 0:
    print('The expression is working well! No opened parenthesis')
else:
    print('This expression is not working! Opened parenthesis')