#INTERATCITVE HELP
#DOCSTRINGS
#ARGUMENTOS OPCIONAIS
#ESCOPO DE VARIAVEL
#RETORNO DE RESULTADOS EM FUNCOES (DEF)


#AJUDA INTERATIVA
help(print)
help(input)
print(input.__doc__) #talvez diferente da do help...

#DOCSTRING
#sao as strings de documentacao...
help(contador)  #vamos supor que eu fiz esse DEF contador...
#para fazer isto logo na linha devbaixo do comando DEF temos que abrir 3x aspas duplas
def contador(i,f,p):
"""
Aqui eu faco a minha DOCSTRING... e posso colocar tipo o meu manual para usar a minha funcao...
essa funcionaliosdade e boa para caso outros usem os nosso codigos.. e checar os codigos de outros tambem...
apos isso aqui eu posso colocaar help(contador) que vai funcionar...
lembrar de apertar enter apos abrir as aspas duplas
"""

#ARGUMENTOS OPCIONAIS
#Apenas colocar a variavel = 0
def boi(a,b,c):
    print(a)

boi(a=1,b=0,c=0)
#dessa forma a funcao vai funcionar... mesmo nao atribuindo valor a ele

#ESCOPO DE VARIAVEIS
#Retratar variaveis globais e locais...
#se eu der um valor dentro de uma DEF esse se torna um valor local de dentro daquela variavel...
y = 3
global1 = 8

def teste():
    global global1 #por cnta desse global aqui, a variavel de baixo deixa de ser local e passa a usar a global, entao vai alterar de 8 para 9...
    global1 = 9 #essa global 1 aqui e uma local...
    x = 8
    print(f'Variavel x e local {x}')
    print(f'Variavel y e global {y}')


print(x) #esta errado pq e uma variavel local, e so funciona dentro de DEF TESTE()
print(y) #funciona pq e global e funciona no programa todo...


#RETORNANDO VALORES (return)

def somar (a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(1,5,4) #10
somar(2,2) #4
somar(6) #6


def somar1 (a=0,b=0):
    s = a+b
    return s
#ASSIM ESSAS VARIAVEIS VAO TER O VALOR DE S...
r1 = somar1(2,3)
r2 = somar1(3,5)

#EXEMPLOS 1

def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
        return f
    #posso retornar qualquer coisa com f...

f1 = fatorial(1)
f2 = fatorial(5)

#EXEMPLOS 2

def parouimpar():
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um numero '))
if parouimpar(num):
    print('Par')
else:
    print('Impar')
