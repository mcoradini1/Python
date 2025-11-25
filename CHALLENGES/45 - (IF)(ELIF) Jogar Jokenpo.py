import random
print('''---------Bem vindo ao Joken-po Do Marlico---------
[1] Pedra
[2] Papel
[3] Tesoura

''')
maquina = random.choice([1,2,3])
print(maquina)
escolha = int(input('Sua escolha e -> '))


if escolha == maquina:
    print('Empatamos hehe')
elif escolha == 1 and maquina ==2:
    print('Voce perdeu eu joguei Papel')
elif escolha ==1 and maquina ==3:
    print('Parabens voce venceu, eu joguei TESOURA')
elif escolha == 2 and maquina ==1:
    print('Parabens voce venceu, eu joguei PEDRA')
elif escolha == 2 and maquina == 3:
    print('Voce perdeu eu joguei TESOURA')
elif escolha ==3 and maquina ==1:
    print('Voce perdeu, eu joguei PEDRA')
elif escolha ==3 and maquina ==2:
    print('Voce venceu, eu joguei PAPEL')
