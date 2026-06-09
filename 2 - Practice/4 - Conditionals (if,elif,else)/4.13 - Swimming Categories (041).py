# ======================================================================================================================
# CHALLENGE 41: Swimming Categories: Check by age(Little one < 9) (Infant < 14) (Junior < 19) (Senior < 25) (Master >25)
# ======================================================================================================================

"""
Challenge: 4.13 - Swimming Categories (041)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - int()
    - if()
    - elif()
    - else()
    - print()

Tags: int(), if(), elif(), else(), print()
Status: ✔️ Completed
"""

age = int(input('Type your age: '))
if age < 9:
    print('The candidate is LITTLE ONE (Lower 9 years old)')
elif 9 < age < 14:
    print('The candidate is INFANT (Between 9 and 14 years old)')
elif 14 <= age < 19:
    print('The candidate is JUNIOR (Between 14 and 19 years old)')
elif 19 <= age < 25:
    print('The candidate is SENIOR (Between 19 and 25 years old)')
else:
    print('The candidate is MASTER (Above 25 years old) ')
