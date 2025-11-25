#mais tradicional e muito trabalho
i = (int(input('Entre um valor ')),
     int(input('Entre outro valor ')),
     int(input('Entre mais um valor ')),
     int(input('Entre o ultimo valor ')))

print(f' -> O numero 9 apareceu {i.count(9)}')
if 3 in i:
    print(f' -> O numero 3 apareceu a primeira vez na {i.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares foram: ')

for n in i:
    if n % 2 == 0:
        print(n, end = ' ')


