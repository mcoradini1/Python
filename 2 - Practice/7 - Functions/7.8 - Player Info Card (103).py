# ======================================================================================================================
# CHALLENGE 103: Player Info Card: Form with optional parameters of player (name, goals)
# ======================================================================================================================

"""
Challenge: 7.8 - Player Info Card (103)
Category: 7 - Collections
Concepts Used:


Tags: if, else
Status: ✔️ Completed
"""

def form(name = '<unknown>',goals=0):
    print(f'The player {name} scored {goals} goals.')

name_variable = input(' Enter your name: ')
goals_variable = str(input(' Enter your goals: '))

if goals_variable.isnumeric():
    goals_variable = int(goals_variable)
else:
    goals_variable = 0

if name_variable.strip() == '':
    form(goals=goals_variable)
else:
    form(name = name_variable,goals=goals_variable)