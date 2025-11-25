lista = list()

for c in range (0,5):
    a = int(input('Digite um valor '))
    if c == 0:
        lista.append(a)
        print('Foi adicionado ao final da lista')
    elif a > lista[-1]: #lista[len(lista)-1] poderia ser assim tb
        lista.append(a)
        print('Foi adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if a <= lista[posicao]:
                lista.insert(posicao,a)
                print(f'Adicionado na posicao {posicao}')
                break

print(f'A lista e {lista}')




#forma de juntar os dois primeiros...
#if c ==0 or a > lista [-1]:
    #lista.append(a)


