n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo valor '))
maior = 0
escolha = 0

while  escolha < 5:
    print('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa\n')
    escolha = int(input('O que deseja efetuar? '))

    if escolha == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    if escolha == 2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    if escolha == 3:
        if n1 > n2:
            maior=n1
        else:
            maior=n2
        print('O maior numero e {}'.format(maior))
    if escolha == 4:
        n1 = int(input('Digite o primeiro valor '))
        n2 = int(input('Digite o segundo valor '))
    if escolha >= 6:
        print('comando invalido')
        escolha = 0

if escolha == 5:
    print('PROGRAMA ENCERRADO')

