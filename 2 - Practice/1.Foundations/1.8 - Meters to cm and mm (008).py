# ========================================================================================================
# CHALLENGE 8: CONVERT FROM METERS TO CENTIMETERS AND MILLIMETERS
# ========================================================================================================

"""
Challenge: 1.8 - Meters to cm and mm (008)
Category: 1.Foundations
Concepts Used:
    - int()
    - .format()

Tags: int(),.format()
Status: ✔️ Completed
"""


m = int(input('Type a measure in meters: '))
print('In centimeters = {}cm\nIn millimeters {}mm'.format(m*100,m*1000))
