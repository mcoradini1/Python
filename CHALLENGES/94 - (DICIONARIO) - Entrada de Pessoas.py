#PROGARMA QUE LE NOME, SEXO E IDADE de varias pessoas em dicionarios
#por os dicionrios em listas
galera = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear() #logo no comeco ja limpo a variavel para no proximo ciclo poder reutilizar...
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0] #considero apenas a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma+= pessoa['idade']
    galera.append(pessoa.copy()) #aqui adiciono as pessoas dentro da lista, para isto uso o append e o .copy (que e como se trabalha nos dicionario para copiar
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Resposta apenas S ou N.')
    if resposta == 'N':
        break
print('-'*60)
media = soma/len(galera)
print(f'A) Pessoas formatadas {len(galera)}')
print(f'B) A media das idades e de {media:5.2f}') #5 casas ao todo e 2 variaveis
print(f'C) As mulheres cadastradas sao ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end = ' ')
print()
print(f'D) As pessoas que estao acima da media sao ', end='')
print()
for t in galera:
    if t['idade'] > media: # aqui poderia fazer igual ao anterior, porem testando esse novo...
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')








