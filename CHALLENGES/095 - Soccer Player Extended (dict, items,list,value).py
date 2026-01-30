#ADD A BIT MORE INFORMATION TO PROGRAM 93, WITH THE OPTION TO ADD MORE PLAYERS: PROVIDE A LIST OF ALL PLAYERS
#GOALS/TOTAL E OPTION TO CHECK TE PLAYER REGISTER NUMBER, CONSIDERING 999 TO CLOSE THE PROGRAM.

team_soccer = list ()
player_soccer = dict ()
matches_soccer = list ()
total = 0
while True:
    player_soccer.clear()
    player_soccer['name'] = str(input('Player name: ')).title()
    tot = int(input(f'How many matches {player_soccer['name']} played? '))
    matches_soccer.clear()
    for c in range(0,tot):
        matches_soccer.append(int(input(f'How many goals {c + 1} in matches: ')))
    player_soccer['goals'] = matches_soccer[:]
    player_soccer['total'] = sum(matches_soccer)
    team_soccer.append(player_soccer.copy())
    while True:
        resp = str(input('Do you want to continue? [Y/N] ')).upper()[0]
        if resp in 'NY':
            break
        print('ERROR! Try again')
    if resp == 'N':
        break
print(team_soccer)
print('-'*60)

for k, v in enumerate(team_soccer):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
    print('-'*60)
    while True:
        search = int(input('Which player do you want to see? (999 to stop) '))
        if search == 999:
            break
        if search >= len(team_soccer):
            print(f'There is no one with the name of {search}')
        else:
            print(f'--- INFO ABOUT --- {team_soccer[search]['name']}:')
            for i, g in enumerate (team_soccer[search]['goals']):
                print(f'     In game {i+1} made {g} goals.')
            print('-'*60)
print('You are welcome!')

