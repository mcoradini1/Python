#somatorio de numeros com parada quando digito 999
n_count = 0
n_sum = 0
n = 0
while n != 999:
    n = int(input('Digite o numero '))
    n_count+=1
    if n != 999:
        n_sum = n_sum + n
print ('A soma foi {}\nNumeros digitados {}'.format(n_sum,n_count-1))

