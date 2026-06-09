# ============================================================
#CHALLENGE 4 - DISSECT VARIABLES WITH THE MOST COMMON METHODS.
# ============================================================

"""
Challenge: 1.4 - Dissect Variables (004)
Category: 1.Foundations
Concepts Used:
    - str()
    - .isspace()
    - .isnumeric()
    - .isalpha()
    - .isalnum()
    - .isupper()
    - .lowercase()
    - .istitle()

Tags: print(), str(), .isspace(), .isnumeric(), .isalpha(), .isalnum(),.isupper(),.lowercase(), .istitle()
Status: ✔️ Completed
"""

n = str(input('Type anything: '))
print('The primitive value of this is ', type(n))
print('Is it only spaces ? ',n.isspace())
print('Is it a number? ', n.isnumeric())
print('Is it a letter? ', n.isalpha())
print('Is it alphanumeric? ', n.isalnum())
print('Is it all uppercase? ', n.isupper())
print('Is it all lowercase? ', n.islower())
print('Is it normal format? ', n.istitle())
