#checar se tem SILVA no nome
nome = str(input('Me fale seu nome completo ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))