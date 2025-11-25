# Terceira meta, curso de python com orientacao a objeto para poder criar interface grafica
#Typos primitivos (4 mais importantes, porem ha mais) - int, str, float, bool...
#float e um ponto flutuante, os chamamos de numeros reais

print('==========DESAFIO 3==========')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

#print('#1 A soma vale', s)
#print('#2 A soma vale {}'.format(s))
# Usando o Format para acrescentar as varievais no meio do texto assim como no ex001. #2 demonstra isso claramente
#1 demonstra o basico usando virgula ou +.

print('A soma entre {} e {} vale {}'.format(n1,n2,s))
#print('A soma entre {0} e {1} vale {2}'.format(n1,n2,s)) pode ser feito assim tb
print(type(s))


print('=========EX EXTRA 1============')
n3 = ('batata')
print(type(n3), n3)


