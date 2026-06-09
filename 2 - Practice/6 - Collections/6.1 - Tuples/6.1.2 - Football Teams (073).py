# ======================================================================================================================
# CHALLENGE 73: Football Teams: gather information from teams provide: first five teams, last four, and where portugal
# ======================================================================================================================

"""
Challenge: 6.1.2 - Football Teams (073)
Category: 6 - Collections
Concepts Used:
    - tuples
    - sorted()
    - .index()


Tags: tuples, sorted(), .index()
Status: ✔️ Completed
"""


tuples_example = ('England', 'Portugal', 'Madeira', 'Italia', 'Brazil', 'Australia', 'Russia', 'Romania')

print(f'The five first teams are: {tuples_example[0:6]}')
print('-'*40)
print(f'The last four teams are: {tuples_example[-4:]}') #-4 till last case
print('-'*40)
print('The teams in alphabetic order is: ', sorted(tuples_example)) #SORT THE TEAMS IN ALPHABETIC ORDER JUST TO PRINT, TUPLES CANNOT BE CHANGED
print('-'*40)
print(tuples_example.index('Portugal')+1)
print('-'*40)