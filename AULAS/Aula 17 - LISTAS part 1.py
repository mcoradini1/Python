#Lista sao mutaveis, tuplas e listas sao semelhantes
#porem tem comandos diferentes para coisas especificas de cada...
# [] < determinam listas



#ADD
lista = []
lista1 = list ()
lanche = ['boi','vaca','leao']
lanche[2] = 'tatu' # isso muda leao para tatu
lanche.append('tamandua') # isso adiciona tamandua ao ultimo termo
lanche.insert(0,'bezerro') #adicioa bezerro no zero, e meche todos para frente...

#DELETAR
del lanche [3] #deletar...
lanche.pop(3) # normalmente o pop e para deletar o ultimo, porem posso por o indice neele
lanche.pop() #deleta o ultimo
lanche.remove('boi') #elimino por termo na lista...
#vao eliminar os elementos e reorgaizar o resto...


#DELETAR TIPS
if 'boi' in lanche: #se pedir para deletar algo que nao existe, o programa da problema...
    lanche.remove('boi')


#USANDO RANGE
valores = list(range(4,11)) #ja estudei o range... ele comeca no 4 e vai ate o 11... e nao vai considerar o 11...
#uma lista chamada valores vai ser criada com os elementos 456789 e 10

#ORGANIAR VALORES
valoresco = [1,4,5,6,9,34,9,2]
valoresco.sort() #por em ordem
valoresco.sort(reverse=True) #reverter para ordem reversa
len(valoresco)

#INDEX para pegar posicao de valor
valoresco.index(9)
#vai me dar a posicao que o primeiro 9 esta...






