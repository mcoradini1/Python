# ====================================================================================================================
# CHALLENGE 40: Student Situation: Check student situation (x < 5 Failed) (5 > x < 6.9 Extra test) (7 > Approved)
# ====================================================================================================================

"""
Challenge: 4.12 - Student Situation (040)
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


n1 = float(input('Type the first result: '))
n2 = float(input('Type the second result: '))

average = (n1 + n2) / 2
if average < 5: #if average >= 5 and average < 7: (USING AND)
    print('{} -> Student FAILED'.format(average))
elif average > 7:
    print('{} -> Student PASS'.format(average))
else:
    print('{} -> Student needs to do extra exam'.format(average))