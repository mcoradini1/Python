def fatorial(n, show=False):
    """

    :param n: Valor a ser considerado para fatorial
    :param show: Mostrar ou nao a sequencia de calculo
    :return: Valor somado de calculo
    """

    f = 1
    for c in range(n,0,-1):
        if show: #Ja assumimos isto como True
            print(c, end='')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

print(fatorial(5,False))
print(help(fatorial))

