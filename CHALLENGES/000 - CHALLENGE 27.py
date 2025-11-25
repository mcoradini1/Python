#Fazer um programa que leia um nome completo, e na resposta, retorne o primeiro e ultimo nome.
nome = str(input('Entre o seu nome ')).strip()
nomecortado = nome.split()
print('Seu primeiro nome e {}'.format(nomecortado[0]))
print('Seu ultimo nome e {}'.format(nomecortado[len(nomecortado)-1]))