# ======================================================================================================================
# CHALLENGE 67: Multiplication Table (Close in case of negative number)
# ======================================================================================================================

"""
Challenge: 5.2.11 - Multiplication Table (067)
Category: 5 - Loops
Concepts Used:
    - while
    - break


Tags: while, break
Status: ✔️ Completed
"""


n = 1
while n > 0:
    print('-' * 60)
    n = int(input('Type the multiplication table of your choice: '))
    print('-' * 60)
    n1 = 1
    while n > 0:
        print('{} * {} = {}'.format(n,n1,n1*n))
        n1 = n1 + 1
        if n1 == 11:
            break
print('Inaccessible value! Shutting down!')
