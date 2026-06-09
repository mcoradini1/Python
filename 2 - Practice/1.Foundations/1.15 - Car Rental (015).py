# ==========================================================================================================
# CHALLENGE 15: CAR RENT PER DAY CONSIDERING 60pounds/day and 0.65pounds/mile
# ==========================================================================================================

"""
Challenge: 1.15 - Car Rental (015)
Category: 1.Foundations
Concepts Used:
    - float()
    - .format()
    - input()

Tags: float(),input(),.format()
Status: ✔️ Completed
"""

kmd = float(input('How many miles expected? '))
diad = float(input('How many days? ') )
km = 0.65
dia = 60

print('With {} miles and {} days'.format(kmd,diad))

print('The total value to pay will be £ {:.2f}'.format((km*kmd)+(diad*dia)))


