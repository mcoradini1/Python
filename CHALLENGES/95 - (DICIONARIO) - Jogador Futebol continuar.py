time = list ()
jogador = dict ()
partidas = list ()
total = 0
while True:
    jogador.clear() #preciso limpar cada vez que fizer...
    jogador['nome'] = str(input('Player name: ')).title()
    tot = int(input(f'quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Gols na {c+1} partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Try again')
    if resp == 'N':
        break
print('-'*60)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
    print('-'*60)
    while True:
        busca = int(input('Mostrar o dado de qual jogador? (999 para parar) '))
        if busca == 999:
            break
        if busca >= len(time):
            print(f'Nao existe um banana com {busca}')
        else:
            print(f'--- LEVANTAMENTO --- {time[busca]['nome']}:')
            for i, g in enumerate (time[busca]['gols']):
                print(f'     No jogo {i+1} fez {g} gols.')
            print('-'*60)
print('Volte sempre!')
