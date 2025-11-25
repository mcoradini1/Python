def fatorial(num, miau=False):
    """

    :param num: Numero que quero usar
    :param miau: Boolean para saber se quero a sequencia completa
    :return: valor final
    """
    resultado = 1
    for f in range(num,1,-1):
        resultado = resultado * f
        if miau == True:
           show(resultado)

    return resultado

def show(resultado):
    print(f'{resultado}', end=' ')

t1= fatorial(5,True)
print(t1)

#TESTANDO O HELPER
#help(fatorial)

#t1 = int(input('Digite um valor '))
#t2 = str(input('Voce quer ver o calculo?? S/N')).upper().strip()

#if t2 in 'S':
#   fatorial(t1,True)
#else:
#    t3 = fatorial(t1,False)
#    print(t3)
