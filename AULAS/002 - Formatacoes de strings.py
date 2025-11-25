n1 = int(input('Entre um valor '))
n2 = int(input('Entre outro valor '))
m = n1/n2
print('a divisao \ne igual {:.3f}' .format(m), end=' >>> ') #posso escrever dentro do end...
#:.3f para por 3 variaveis apenas
#end='' para colcoar a linha de baixo em cima, nao ter paragrafo
#\n serve para por quebra de linha
print('A goiaba e branca')

print('\n\n\n\n Aqui vai algumas formatacoes')
nome = 'Jose'
idade = 33
salario = 1256.365484
print(f'O {nome} e tem {idade} e o aslario e {salario:.2f}') #casas apos a virgula no salario
print(f'{nome:-^20}') #centralizado no meio de 20 ^
print(f'{nome:20}') #20 espacos na frente
print(f'{nome:^20}') #20 espacos porem centralizado
print(f'{nome:-<20}') #20 espacos porem para olado direito com o hifen

