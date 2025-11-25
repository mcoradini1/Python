num = [2,5,9,1]
num.append(7)
num.sort()
print(num)
num.insert(2,83)
num.remove(2)
print(f'Ha {len(num)} na lista\n\n')
print(num)

for v in num:    #assim pego apenas os numeros na lista
    print(f'{v}',  end = ' ')

for c, v in enumerate(num): # eu pego a posicao do valor na lista com o enumerate
    print(f'{c}e o meu numerador\n {v} e o meu numero')

valores = list() #adicionando varios faceis...
for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#PECULIARIADADE PYTON
#a partir do momento que eu igualo uma lista a outra, ambas tem uma ligacao pra sempre...
a = [2,3,4,7]
b = a
b[2] = 8
#aqui alterei apenas na lista b, porem a lista a tambem foi mudada...

#COPIAR LISTA
b = a[:] #aqui pego todos elementos de A
#b diferente de a aqui
