# ====================================================================================================================
# CHALLENGE 38: Greater Value: Check the greater value between two floats
# ====================================================================================================================

"""
Challenge: 4.10 - Greater Value (038)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - float()
    - if()
    - elif()
    - else()
    - print()

Tags: float(), if(), elif(), else(), print()
Status: ✔️ Completed
"""

n1 = float(input('Type the first number: '))
n2 = float(input('Type the second number: '))

if n1 > n2:
    print ('The first number is greater than the second number')
elif n1 < n2:
    print ('The second number is greater than the first number')
else:
    print ('They are equal')