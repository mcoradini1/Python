# ==============================================================================================================
# CHALLENGE 31: Bus Travel Price: Short Distance (< 200 Miles) - 0.50£/mile, Long Distance (>200) - 0.45£/miles
# ==============================================================================================================

"""
Challenge: 4.3 - Bus Travel Price (031)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - float()
    - if()
    - else()
    - .format
    - print()

Tags: float(), if(), else(), .format, print()
Status: ✔️ Completed
"""


distance = float(input('Type the travel distance: '))
if distance <= 200:
    price = distance * 0.50
    print('Your travel will be {:.2f}£'.format(price))
else:
    price = distance * 0.45
    print('Your travel will be {:.2f}£'.format(price))

