
# ==========================================================================================================
# CHALLENGE 10: PROGRAM TO CONVERT FROM REAIS (BRAZIL) TO DOLLARS (USA) - CONSIDERING 1 DOLLAR = 3.27 REAIS
# ==========================================================================================================

"""
Challenge: 1.10 - REAL to DOLLAR (010)
Category: 1.Foundations
Concepts Used:
    - float()
    - .format()

Tags: float(),input(),.format()
Status: ✔️ Completed
"""


n = float(input('Type the amount of REAIS to convert to DOLLARS: '))
d = 3.27
m1 = n/d
m2 = n//d
m3 = m1 - m2
m4 = m3 * d

print('\nYou can buy {}, and it will remain {:.3f} reais'.format(m2,m4))
print('\nIn a simpler way you can buy {:.3f}'.format(n/d))