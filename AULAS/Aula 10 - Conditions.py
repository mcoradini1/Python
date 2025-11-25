nome = str(input('Qual e o seu nome? ')).strip()
print(nome) #apenas para testar
nome = nome.capitalize()
print(nome) #apenas para testar se tava certo
if nome == 'Marlon':
    print('Que nome bonito voce tem {}'.format(nome))
else:
    print('Seu nome e bem cool {}'.format(nome))
print('Bom dia {}!'.format(nome))

# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: