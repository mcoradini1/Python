#LER um numero inteiro e usar algumas base de conversao (1 binario, 2 octal e 3 hexadecimal)
num = int(input('Entre um numero '))
base = int(input('''Qual vai ser a base de conversao utilizada? 
[1] Binario
[2] Octal
[3] Hexadecimal 
-> '''))
if base == 1:
    print('O valor em BINARIO e -> {}'.format(bin(num)[2:])) # [ O 2: serve para ignorar as duas letras iniciais... que vao ser 0b de binario
elif base == 2:
    print('O valor em OCTAL e -> {}'.format(oct(num))) # o mesmo pode colocar aqui e vai cortar o 0o..
elif base == 3:
    print('O valor em HEXADECIMAL e -> {}'.format(hex(num))) # o mesmo pode se por aqui porem nao coloquei...
else:
    print('Numero nao identificado')
