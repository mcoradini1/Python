#EXEMPLO 1:

pessoas = {'nome' : 'Gustavo', 'sexo': 'M',  'Idade': 22}
pessoas['peso'] = 98.5 #adicionando um elemento...
print(f'O {pessoas['nome']} tem {pessoas['Idade']} anos')

for k in pessoas.keys(): #para cada uma das chaves mostrar... posso trocar o keys por values
    print(k)

#no dicionario nao temos ENUMERATE, eu tenho o ITEMS...

for k, v in pessoas.items():
    print(f'{k} and {v}')

#EXEMPLO 2:
estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Entre a sigla '))
    estado['sigla'] = str(input('Entre o estado '))
    brasil.append(estado) #isto aqui causara problema, pois todos os tres serao o mesmo... pois a conexao entre eles
    brasil.append(estado[:]) #dessa forma nao da certo, pois isto apenas funcona par listas
#METODO NO DICIONARIO .COPY
    brasil.append(estado.copy()) #METDO INTERNO PARA FAZER EM DICIONARIOS
    print(brasil) #assim mostraria da forma tradiucional

#MOSTRANDO DE UMA FORMA MELHOR:

for e in brasil: #pegar cada valor da lista
    for k, v in e.items(): #pegar cada valor do dicionario em relacao a lista que ele esta...
        print(f'O campo {k} tem valor {v}.')
