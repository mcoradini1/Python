# ======================================================================================================================
# CHALLENGE 93: Soccer Player Registration; Show how many matches and goals
# ======================================================================================================================

"""
Challenge: 6.3.5 - Employee Registration (094)
Category: 6 - Collections
Concepts Used:
    - dict
    - if()
    - for
    - items()


Tags: dict, if(), for, items()
Status: ✔️ Completed
"""

player_soccer = dict ()
goals = list ()
total = 0

player_soccer['Name'] = str(input('Player name: ')).title()
soccer_matches = int(input(f'How many matches {player_soccer['Name']} played? '))
for c in range(0, soccer_matches):
    goals.append(int(input(f'How many goals {c+1} in matches: ')))
    total = total + goals[c]
player_soccer['Goals'] = goals
player_soccer['Total'] = total

print('-'*60)
print(player_soccer)
print('-'*60)
for c, v in player_soccer.items():
    print(f'The {c} is {v}')
print('-'*60)
print(f'The player {player_soccer['Name']} played {soccer_matches} matches')
for n1,n2 in enumerate(goals):
    print(f'In the {n1+1} game he/she scored {n2} goals')

