# dentro da tupla cada string e uma lista de letras... por isso consigo fazer a parte de baixo
palavras = ('batata', 'caramelo', 'chinelo', 'tomate', 'alface', 'frango', 'cebola', 'pao', 'cebolinha')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end = ' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end =' ')

