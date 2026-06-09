# ==========================================================================================================
# CHALLENGE 17: ALGORITHM TO READ ADJACENT SIDE, OPPOSITE SIDE AND FINDS HYPOTENUSE
# ==========================================================================================================

"""
Challenge: 3.2 - Hypotenuse (017)
Category: 3 - Numbers, Math and Logic
Concepts Used:
    - float()
    - .format()
    - input()
    - import math

Tags: float(),input(),.format(), hypot()
Status: ✔️ Completed
"""

import math

co = float(input('Enter the opposite side: '))
ca = float(input('Enter the adjacent side: '))
h = (ca**2+co**2)**(1/2)
print ('The Hypotenuse is {:.2f}'.format(h))

print('The Hypotenuse is {:.2f}'.format(math.hypot(co,ca)))


