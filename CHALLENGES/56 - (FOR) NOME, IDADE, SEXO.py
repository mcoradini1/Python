#4 PESSOAS
idade_media = 0
velho = 0
nome_velho = 0
mulheres_20 = 0 #mulheres com menos de 20 anos
for c in range (1,3):
    nome = str(input('Qual o nome do {} '.format(c)))
    idade = int(input('Qual a idade do {} '.format(c)))
    sexo = int(input('Qual o sexo do {} \n[1] Masculino\n[2] Feminino\n'.format(c)))
    idade_media+= idade
    if sexo == 2 and idade<20:
        mulheres_20+=1
    if idade > velho and sexo == 1:
        velho = idade
        nome_velho = nome

print('A media de idade do grupo e de {}\nO homem mais velho tem o nome de {} e {} anos\nTemos {} mulheres com menos de 20 anos'.format(idade_media/2,nome_velho,velho,mulheres_20))
