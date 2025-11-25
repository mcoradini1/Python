jogador = dict ()
goals = list ()
total = 0

jogador['NAME'] = str(input('Player name: ')).title()
partidas = int(input(f'quantas partidas {jogador['NAME']} jogou? '))
for c in range(0,partidas):
    goals.append(int(input(f'Gols na {c+1} partida: ')))
    total = total + goals[c]
jogador['GOALS'] = goals
jogador['TOTAL'] = total

print('-'*60)
print(jogador)
print('-'*60)
for c, v in jogador.items():
    print(f'O campo {c} tem {v}')
print('-'*60)
print(f'The player {jogador['NAME']} jogou {partidas} partidas')
for n1,n2 in enumerate(goals):
    print(f'Na partida {n1+1} temos {n2} goals')

