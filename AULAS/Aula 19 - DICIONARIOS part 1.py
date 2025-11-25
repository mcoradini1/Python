#aqui tenho indices literais (coloco nomes)
# {} determinam os dicionarios.

#EXEMPLO INICIAL
dados1 = {}
dados = dict()
dados = {'nome':'Pedro', 'idade':25} #dicionario com 2 termos (o termo '0' nomeado de nome, com Pedro, e o termo '1' nomeado idade)
filme = dict()

#PRINT NOS DADOS
print(dados['nome']) # PEDRO
print(dados['Idade']) #25

#ADICIONAR
dados['sexo'] = 'M' #Aqui nao uso APPEND

#DELETAR
del dados['idade']

#
print(dados.values()) # todos valores do dicionario (Pedro e 25)
print(dados.keys()) # vai retornar nome e idade ( as chaves)
print(dados.items) # vai pegar os dois Keys e values


#FOR EXEMPLO
for k,v in dados.items():
    print(f'O {k} e {v}') #vai mostar o nome e pedro a idade e 25 para todos que eu tiver...

#JUNTANDO LISTAS COM DICIONARIOS
#imaginar o dicionario dados dentro de uma lista
print(lista[0]['idade']) # pegaria apenas a idade no index 0...
