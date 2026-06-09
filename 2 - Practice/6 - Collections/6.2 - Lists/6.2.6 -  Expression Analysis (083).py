# ======================================================================================================================
# CHALLENGE 83: Expression Analysis: Read analyse expressions and tell if it is alright (specifically parenthesis)
# ======================================================================================================================

"""
Challenge: 6.2.6 -  Expression Analysis (083)
Category: 6 - Collections
Concepts Used:
    - list
    - .append()
    - if()
    - else()
    - for()
    - range


Tags: list, .append(), if(), else(), for(), range
Status: ✔️ Completed
"""

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