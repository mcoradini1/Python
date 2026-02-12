#A PROGRAM TO PREPARE A FORM WITH OPTIONAL PARAMETER OF PLAYERS BY NAME AL GOALS

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