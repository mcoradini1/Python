#Um programa que coloca os alunos em uma ordem de apresentacao
import random #aqui poderia ser from random import shuffle
n1 = str(input('Entre o nome do primeiro aluno: '))
n2 = str(input('Entre o nome do segundo aluno: '))
n3 = str(input('Entre o nome do terceiro aluno: '))
n4 = str(input('Entre o nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
print('o nome dos alunos em lista e {}'.format(lista))
random.shuffle(lista) #Poderia ser apenas shuffle, caso eu colocassse la em cima diferente
print('A nova ordem ficou em {} '.format(lista))

