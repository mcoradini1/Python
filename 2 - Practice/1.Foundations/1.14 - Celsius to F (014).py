# ==========================================================================================================
# CHALLENGE 14: CONVERT CELSIUS TO F
# ==========================================================================================================

"""
Challenge: 1.14 - Celsius to F (014)
Category: 1.Foundations
Concepts Used:
    - float()
    - .format()
    - input()

Tags: float(),input(),.format()
Status: ✔️ Completed
"""

c = float(input('Inform the temperature in C: '))
f = ((9*c)/5)+32
print('The temperature is {:.2f} F'.format(f))
