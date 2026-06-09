# ==========================================================================================================
# CHALLENGE 29: Traffic Ticket: if above 80m/h (fined), 7 pounds per mile above 60m/h
# ==========================================================================================================

"""
Challenge: 4.1 - Traffic Ticket (029)
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


speed = float(input('Type the speed? '))
if speed > 80:
    fine = (speed - 80) * 7
    print('You got fined in {:.2f} £'.format(fine))
else:
    print('You are alright, please keep your travel.')
print('\n\nHave a good day! ')