# Programa que leia uma frase e mostre
#quantas vezes a letra A aparece
#Em que posicao a primeira vez
#Em que posicao a ultima vez

frase = str(input('Digite a sua frase ')).strip().upper()
#frase: str = 'A barata diz a macaco'.upper()
#print(frase)
print('Na sua frase tem {} letras (A)'.format(frase.count('A')))
print('Na sua frase a primeira letra a acontece {}'.format(frase.find('A')+1))
print('Na sua frase a ultima letra a acontece {}'.format(frase.rfind('A')+1))








