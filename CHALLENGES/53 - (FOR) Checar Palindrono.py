#cHECAR SE E PALINDROmO... coisas lidas de traz pra frente sendo o mesmo...

p = input('Qual a sua frase? ').strip().upper()
palavras = p.split() #divido em palavras
juntas = ''.join(palavras) #junto elas com sem espaco nesse caso...
inverso = ''
for letras in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letras]

print(juntas, inverso)

if inverso == juntas:
    print('E um palindromo')
else:
    print('Nao e um Palindromo')

# poderia apenas por inverso = junto[::-1] so isto inverteria a palavra, e naoprecisaria de todos os comandos ehhe