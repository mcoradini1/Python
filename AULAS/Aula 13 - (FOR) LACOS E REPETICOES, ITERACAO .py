#for c in range(1,10,2): fazer um laco que funcione com isto...
#ele comecano primeiro e termina no segundo, e o terceiro como ele vai subindo... no caso a cima de 2 em 2)
# range (0, 3), isso aqui tem 3 espacos, pois nao consiedra oultimo numero

#PRECISA DE SER REDONDINHO PRECISO DE TER LIMITES
#estrutura de repetico com teste logico

for c in range(1,6): #ele faz 5 vezes pq nao considera o ultimo numero
    print('teste')
print('acabou')

#Esse aqui e outro teste...
for c in range(0,6):
    print(c)

#aqui o -1 vai dizer como ele vai contar...
for c in range(6, 0, -1):
    print(c)
print('FIM')

#programa teste 1
n = int(input('Digite um numero: '))
for b in range (0, n+1):
    print(b)
print('FIM')

#programa teste 2 (usando variaveis dentro do comando
i = int(input('INICIO'))
f = int(input('FIM'))
co = int(input('Contagem'))
for c in range (i, f+1, co):
    print(c)
print('fim')

#programa teste 3
s = 0
for c in range(0,4):
    n = int(input('Digite um numero '))
    s = s + n # s+= n mesma coisa
print('O somatorio deu {}'.format(s))
