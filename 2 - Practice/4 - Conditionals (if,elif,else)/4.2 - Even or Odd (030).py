# ==========================================================================================================
# CHALLENGE 30: Even or Odd
# ==========================================================================================================

"""
Challenge: 4.2 - Even or Odd (030)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - int()
    - if()
    - else()
    - .format
    - print()

Tags: float(), if(), else(), .format, print()
Status: ✔️ Completed
"""

num = int(input('Type a number: '))
check = num % 2
if check==0:
    print('The number {} is even'.format(num))
else:
    print('The number {} is odd'.format(num))