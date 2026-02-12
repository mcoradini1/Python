#A PROGRAM THAT HAS TUPLE WITH NAME OF TEAMS I WILL GATHER INFORMATION FROM THEM:
#FIRST 5 TEAMS, LAST 4 TEAMS, WHICH POSITION IS PORTUGAL

tuples_example = ('England', 'Portugal', 'Madeira', 'Italia', 'Brazil', 'Australia', 'Russia', 'Romania')

print(f'The five first teams are: {tuples_example[0:6]}')
print('-'*40)
print(f'The last four teams are: {tuples_example[-4:]}') #-4 ate o ultimo nesse caso
print('-'*40)
print('The teams in alphabetic order is: ', sorted(tuples_example)) #SORT THE TEAMS IN ALPHABETIC ORDER JUST TO PRINT, TUPLES CANNOT BE CHANGED
print('-'*40)
print(tuples_example.index('Portugal')+1)
print('-'*40)