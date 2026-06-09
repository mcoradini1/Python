# ========================================================================================================
#CHALLENGE 6: TYPE A NUMBER, THEN SHOW 2x, 3x and SQUARE ROOT OF THE NUMBER
# ========================================================================================================

"""
Challenge: 1.6 - Math Foundation (006)
Category: 1.Foundations
Concepts Used:
    - int()
    - input()
    - * (multiplication)
    - ** (potency)
    - / (division)


Tags: int(),input()
Status: ✔️ Completed
"""

n = int(input('Type a number: '))
d = n*2
t = n*3
q = n**(1/2)
print('The number = {}\n2x = {}\n3x = {}\nSquare root = {}'.format(n,d,t,q))