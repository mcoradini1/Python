# ======================================================================================================================
# CHALLENGE 66: SUM with break: Sane as 5.2.9 but using break (999 to stop, not considering in the sum)
# ======================================================================================================================

"""
Challenge: 5.2.10 - SUM with break (066)
Category: 5 - Loops
Concepts Used:
    - while
    - break


Tags: while, break
Status: ✔️ Completed
"""



n_count = 0
n_sum = 0
n = 0
while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    n_count+=1
    n_sum = n_sum + n

print ('The sum is {}\nYou typed {} numbers'.format(n_sum,n_count-1))

