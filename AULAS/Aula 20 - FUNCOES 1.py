funcao ou def
#sao relacionadas em funcoes (tem funcionalidades)
#print e uma funcao que existe...

#posso criar uma linha na tela com print('-'60)

lembrar que tenho parenteses na frente...
Entre o def e o programa principal preciso deixar 2 linhas, se nao o programa reclama

def mostraLinha():
    print('-----------------------')


mostraLinha()
print('MIAU')
mostraLinha()

def mensagem(msg):
    print('-'*60)
    print(msg)
    print('-'*60)

def soma(a,b):
    s = a + b
    print(s)
    print(f' A soma A + B e igual a {}')

#progrma principal
soma (4, 5)
soma(8, 9)
soma(2, 1)
soma(4) #problema pois temos 2 termos aqui
soma(a=2,b=3) #assim funciona bem tambem
soma(a=3,6) #assim n funciona

#EMPACOTANDO PARAMETROS
def contador1 (*num): #vai seguir o numero de variaveis que o programa vai precisar...
    #ele vai criar uma tupla com todos valores

#EXEMPLO 1
def contador(*num):
    for valor in num:
        print(f'{valor}', end='')
    print('FIM!')


contador(2, 1, 4, 3)
contador(2,3)
contador(8,6,0,0,0,8,4,32)


#TRABALHANDO COM LISTAS (isso nao e desempacotar...)
def dobra(lista)
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos +=1


valores = [7,8,8,5,7,89]
dobra(valores)
print(valores)

def soma2(*valores):
    s = 0
    for num in valores:
        s+= num
        print(f'somando {valores} temos {s}')