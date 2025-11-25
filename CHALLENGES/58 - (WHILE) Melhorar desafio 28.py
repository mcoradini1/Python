#dessa vez poderemos dar papite ate acertar porem de 0 a 10
import random
palpites = 0
palpite = -1
maquina = random.randint(0,10)
print(maquina)
while palpite != maquina:
    palpite = int(input('Qual e o seu palpite? '))
    if palpite != maquina:
        print('ERRADOOOOOOOO')
        palpites+=1
print('Finalmente voce conseguiu eu pensei o numero {}, voce acertou em {} tentativas'.format(maquina,palpites))




