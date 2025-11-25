#Primeiro termo (determina aonde comeco, a a acao e como isso vai somando...
t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
decimo = t + (11-1)* r #formula matematica de PA, para acahr o decimo termo.. poderia ser para qualquer termo
for c in range (t, decimo, r):
    print(c, end = ' -> ')
print('ACABOU')


