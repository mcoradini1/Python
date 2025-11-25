from time import sleep
x = 0
def contador():
    print(f'A) ', end ='')
    for c in range (0,11):
        print(f'{c}', end =' ')
        sleep(x)
    print(f'\nB) ', end='')
    for b in range (20,-1,-2):
        print(f'{b}', end=' ')
        sleep(x)
    inicio1 = int(input('\nDigite o inicio '))
    fim2 = int(input('Digite o fim '))
    passo3 = int(input('Digite o passo '))
    print('C) ', end= '')
    if inicio1 < fim2:
        if passo3 == 0:
            passo3 =1
        print(f'Contando de {inicio1} ate {fim2} em {passo3} ')
        for d in range(inicio1, fim2+1, passo3):
            print(f'{d} ', end = '')
            sleep(x)

    else:
        if passo3 == 0:
            passo3 =1
        print(f'Contando de {inicio1} ate {fim2} em {passo3} ')
        for d in range(inicio1, fim2-1, -passo3):
            print(f'{d} ', end = '')
            sleep(x)


contador()