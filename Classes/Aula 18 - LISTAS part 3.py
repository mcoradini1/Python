#LISTAS DENTRO DE LISTAS
#funcionamento das listas compostas

pessoas = [['Pedro',25], ['Maria',19], ['Joao', 32]]
#lista pessoas tem a lista de PEDRO no termo 0...
#A lista de pedro tem 25 no termo 1...

print(pessoas[0][0]) # Pedro e a resposta
print(pessoas[1][1]) # 19
print(pessoas[2][0]) #joao
print(pessoas[1]) # [Maria e 19]
#mais para frente vou poder mudar esses numeros com os dicionarios... mas no momento usamos os numeros para enciontrar

#ERRADO  ----------------------------------------------------------------------
#Fazendo assim quando for imprimir no final vai estar Susana 28 e Susana 28, por conta do vinculo entre as listas
pessoa = list ()
pessoa.append('Marlon')
pessoa.append('30')
galera = list ()
galera.append(pessoa) # aqui devo por galera.append(teste[:]) preciso fazer uma copia,pois se eu udar a primeira estrutura
pessoa[0] = 'Susana'   # que e o testem automaticamente eu mudo a segunda tb... exceto se eu copiar...
pessoa[1] = 28
galera.append(pessoa) #aqui devo por galera.append(teste[:])
print(galera)

#COMPREENDENDO MAIS  ----------------------------------------------------------------------
galera1 = [['Joao', 19], ['Marlon', 30], ['Susana', 28], ['Gabi', 19]]
print(galera1) #aparece todos
print(galera[2][1]) # 28


#FOR ----------------------------------------------------------------------
for p in galera: #para cada pessoa em galera
    print(p) #aparece o nome e idade
    print(p[1]) #aarece so a idade de cada...
    print(f'{p[0]} tem {p[1]} anos de idade')

#LISTA SECUNDARIA EXEMPLO  ----------------------------------------------------------------------
galera2 = list ()
dado = list ()
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade ')))
    galera2.append(dado[:]) #se nao colocar copia as listas ficam ligadas
    dado.clear() #se estiverem ligadas as listas, nao vai ter nada em galera2
print(galera2)

totalmaior = totalmenor = 0 #variaveis simples... posso fazer isso igualar elas entre si de boa
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        totalmaior+=1
    else:
        print(f'{p[1]} e menor de idade')
        totalmenor+=1
print(f'O total de maiores deu {totalmaior} e o menores deu {totalmenor}')
