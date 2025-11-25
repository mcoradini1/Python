lista = list ()
lista_par = list ()
lista_impar = list()
n = int(input('Quantos valores queres adicionar? '))
for c in range (0,n):
    lista.append(int(input(f'Digite o {c} numero ')))
for c1 in lista:
    if c1 % 2 == 0:
        lista_par.append(c1)
    else:
        lista_impar.append(c1)

print(f'-> Pares {lista_par}\n-> Impares {lista_impar}')

