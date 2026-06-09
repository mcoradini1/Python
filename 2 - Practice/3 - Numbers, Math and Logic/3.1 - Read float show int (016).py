# ==========================================================================================================
# CHALLENGE 16: AN ALGORITHM TO READ A FLOAD VARIABLE AND SHOW ONLY THE INTEGER PART.
# ==========================================================================================================

"""
Challenge: 3.1 - Read float show int (016)
Category: 3 - Numbers, Math and Logic
Concepts Used:
    - float()
    - .format()
    - input()
    - import math
    - from math import trunc()

Tags: float(),input(),.format(), trunc()
Status: ✔️ Completed
"""


#import math (could use that)
from math import trunc

r = float(input('Enter a float number: '))
print('First method - Your number is -> {}'.format(int(r)))

print('\n\nSecond Method - Your numbers is {} \nIts whole part is {}'.format(r, trunc(r)))

#print('\n\nSecond Method - Your numbers is {} \nIts whole part is {}'.format(r, math.trunc(r)))

#THIS SECOND FORM I WOULD USE IN CASE I HAD IMPORT THE WHOLE LIBRARY MATH (TOO MUCH FOR JUST A FUNCTION)