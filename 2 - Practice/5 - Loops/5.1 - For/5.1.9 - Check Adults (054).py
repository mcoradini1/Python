# ======================================================================================================================
# CHALLENGE 54: Check Adults: Check if the person is underage ( < 18 ) or an adult ( > 18)
# ======================================================================================================================

"""
Challenge: 5.1.9 - Check Adults (054)
Category: 5 - Loops
Concepts Used:
    - for
    - range()
    - if()
    - import datetime
    - date.today().year

Tags: for, range(), if(), import datetime, date.today().year
Status: ✔️ Completed
"""


import datetime
today = datetime.date.today().year
adult = 0
for c in range (1,8):
    year = int(input('Type the year of birthday of the {} person '.format(c)))
    if today - year >= 18:
        adult += 1
print('In this list we have: \n{} Adult(s) (18+)\n{} Underage(s) (18-)'.format(adult, 7 - adult))