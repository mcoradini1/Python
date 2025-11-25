#sequencia de fibonatti e aquela que soma o primeiro com o segundo para dar o resultado doterceiro... sendo o elemento 0 = 1, 1 = 1, 2 = 1, 3 = 2
# 0 1 1 2 3 5 8 13 21 34
print('-'*60)
fib = int(input('Quantos numeros da sequencia voce quer ver? '))
print('-'*60)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end = '')
cont = 3
while cont <= fib:
    t3 = t1 + t2
    print('-> {} '.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')


