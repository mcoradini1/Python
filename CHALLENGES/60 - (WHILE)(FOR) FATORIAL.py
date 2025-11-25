n = int(input('Entre o numero '))
fatorial = n
n1 = n
while not n == 1:
    fatorial = fatorial * (n-1)
    n-=1
print(fatorial)


n1 = int(input('\n\n\nEntre um numero '))
fatorial1 = n1

for c in range (n1,1,-1):
    fatorial1 = fatorial1 * (n1-1)
    n1-=1
print(fatorial1)