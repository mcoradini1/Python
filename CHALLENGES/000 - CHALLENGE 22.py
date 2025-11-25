#Programa para ler um nome e mostrar o nome com todas maiusculas, todas minusculas, quantas letras sem contar espacos e
#quantas letras o primeiro nome
nome = str(input('Me de o seu nome: ')).strip() #.strip e para tirar os espacos docomeco e do fim
print('Seu nome em CAPS e {}'.format(nome.upper()))
print('Seu nome todo em MIN e {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

#Tenho dois metodos aqui em baixo para poder fazer coisas semelhantes...
print('Seu primeiro nome tem {}'.format(nome.find(' '))) #vai achar o primeiro espaco... E vai contar qual
#espaco esse aqui ta... Por isso funciona...
separa = nome.split()
print('Seu prieiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#essa segunda forma e melhor de se fazer



