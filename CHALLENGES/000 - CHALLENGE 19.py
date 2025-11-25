import random
# escolher um nome aleatorio da lista
# poderia por apenas from random import choice, porem teria que tirar o random no escolhido
n1 = str(input('Entre o primeiro aluno: '))
n2 = str(input('Entre o segundo aluno: '))
n3 = str(input('Entre o terceiro aluno: '))
n4 = str(input('Entre o quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)   #aqui ficaria escolhido = choice(lista)
print('O aluno que vai apresentar vai ser o {}'.format(escolhido))