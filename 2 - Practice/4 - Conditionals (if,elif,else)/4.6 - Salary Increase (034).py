# ==============================================================================================================
# CHALLENGE 34: Salary Increase: 10% increase 5.1 - For ( > 1250,00 £) and 15% 5.1 - For lower.
# ==============================================================================================================

"""
Challenge: 4.6 - Salary Increase (034)
Category: 4 - Conditionals (if,elif,else)
Concepts Used:
    - float()
    - if()
    - else()
    - .format
    - print()


Tags: float(), if(), else(), .format, print()
Status: ✔️ Completed
"""


salary = float(input('What is your salary: ? '))
if salary > 1250:
    print('The new salary is {} \nA 10% increase '.format(salary + (salary * 0.1)))
    print('{:.2f} * 10% = {:.2f}'.format(salary, salary * 0.10))
else:
    print('{:.2f} * 15% = {:.2f}'.format(salary, salary * 0.15))
    print('The new salary is {} \nA 15% increase'.format(salary + (salary * 0.15)))