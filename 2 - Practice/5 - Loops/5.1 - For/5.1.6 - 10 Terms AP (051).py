# ======================================================================================================================
# CHALLENGE 51: 10 Terms AP: Find out 1 terms of an Arithmetic Progression
# ======================================================================================================================

"""
Challenge: 5.1.6 - 10 Terms AP (051)
Category: 5 - Loops
Concepts Used:
    - for
    - range()


Tags: for, range()
Status: ✔️ Completed
"""


t = int(input('First term: '))
r = int(input('Rate: '))

term_10th = t + (11 - 1) * r #THIS IS THE EQUATION TO FIND THE 10TH TERM
for c in range (t, term_10th, r): #REMEMBER: First term (starts), last term (end), rate (how much will sum)
    print(c, end = ' -> ')
print('FINISHED')


