import random
count_victories = 0

while True:
    eu_num = int(input('Digite o seu numero '))
    while True:
        eu_escolha = str(input('Par ou Impar? ')).upper()
        if eu_escolha == 'PAR' or eu_escolha == 'IMPAR':
            break
    computador_num = random.randint(0,10)
    check = eu_num + computador_num
    if check%2 == 0:
        if eu_escolha == 'PAR':
            print(f'Voce venceu, voce jogou {eu_num}, e eu joguei {computador_num} o que da {check} que e {eu_escolha} Venceu!\n\n')
            count_victories += 1
        else:
            print(f'Perdeu, nossa soma deu {check} e voce colocou {eu_escolha}, voce teve {count_victories} vitorias consecutivas\n\n')
            break

    else:
        if eu_escolha == 'IMPAR':
            print(f'Voce venceu, voce jogou {eu_num}, e eu joguei {computador_num} o que da {check} que e {eu_escolha} Venceu!\n\n')
            count_victories += 1
        else:
            print(f'Perdeu, nossa soma deu {check} e voce colocou {eu_escolha}, voce teve {count_victories} vitorias consecutivas\n\n')
            break








