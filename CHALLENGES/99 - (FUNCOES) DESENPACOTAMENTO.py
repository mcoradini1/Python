from time import sleep
tempo = 0.3

def maior(*num):
    print('-'*60)
    maior1 = 0
    for valor in num:
        print(f'{valor} ', end='')
        sleep(tempo)
        if valor >= maior1:
            maior1 = valor
    print(f'\nO maior valor e {maior1}')
    print('-'*60)


maior(1,2,3,4,5,6)
maior(2,4,7,0,124,5,32,8,0)
maior(1,2,2,2,3,4,6,9,98,675)