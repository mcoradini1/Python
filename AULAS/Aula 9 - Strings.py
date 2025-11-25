frase = 'Curso em Video PythOn'
print(frase[3]) #pego apenas o elemento 3 da string, sendo C o elemento 0...
print(frase[3:13]) #pego do elemento 3 ate o elemento 13 (nao considera o elemento 13)
print(frase[::2]) #sem comeco e sem fim, indo de 2 em 2
print(frase.count('o')) #contar o numero de letras em uma string (case sensitive, devo considerar)
print(frase.upper().count('O')) #Coloco a minha string toda em maiuscula e entao conto as letras O, isso facilita

.upper()[0] # neste caso pego apenas a primeira letra

print(frase.lower().count('o')) #Coloco tudo em minusculo e conto, mais facil
print(frase.replace('PythOn', 'Android'))
print(frase.find('video')) #se caso der -1, isso quer dizer que ano encontrou
print(frase.find('Video')) #aqui mostra onde comeca, no caso real e no 9 (assim seria menos geral de fazer)
print(frase.lower().find('video')) #assim e uma forma mais esperta de fazer... poderia usar o upper tb...

#procurar a letra A, comecando da frente e comecando por traz...
#print('Frase teste {}'.format(variavel.find('A')+1))
#print('Frase teste {}'.format(variavel.rfind('A')+1))


print("""\n\nEsse e apenas um teste hehe ddsfdsfsdfsdfdsf
dfsdfdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfds
fdfsdfsdfdsfsdfsdfsdfsdfsdfsdfsdfsd """) #Uso as 3 vezes aspas para captar textos diretos assim...