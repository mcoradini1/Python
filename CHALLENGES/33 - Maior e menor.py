#checar o maior e menor numero de 3 numeros citados
a = int(input('Entre um numero '))
b = int(input('Entre outro numero '))
c = int(input('Entre o ultimo numero '))
lista = [a, b, c]
print(lista)
if a<=c and a<=b:
    menor = a
if b<=a and b<=c:
    menor = b
if c<=a and c<=b:
    menor = c
if a>=b and a>=c:
    maior = a
if b>=a and b>=c:
    maior  = b
if c>=a and c>=b:
    maior = c

print('\n\nO maior e {}\nO menor e {}'.format(maior,menor))