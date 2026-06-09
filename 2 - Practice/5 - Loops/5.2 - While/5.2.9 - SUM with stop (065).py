# ======================================================================================================================
# CHALLENGE 65: SUM with stop: Use stop criteria (999 will stop)
# ======================================================================================================================

"""
Challenge: 5.2.9 - SUM with stop (065)
Category: 5 - Loops
Concepts Used:
    - while


Tags: while
Status: ✔️ Completed
"""

n_count = 0
n_sum = 0
n = 0
while n != 999:
    n = int(input('Type a number: '))
    n_count+=1
    if n != 999:
        n_sum = n_sum + n
print ('The sum is {}\nYou typed {} numbers'.format(n_sum,n_count-1))

