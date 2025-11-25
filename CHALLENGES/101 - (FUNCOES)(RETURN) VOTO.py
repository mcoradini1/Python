def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if ano > 65:
        f = f'Com {idade} anos o voto e OPCIONAL'
        return f
    elif ano < 18:
        f = f'Com {idade} anos o voto e NEGADO'
        return f
    else:
        f = f'Com {idade} anos o voto e OBRIGATORIO'
        return f

entrada = voto(int(input('Digite seu ano de nascimento ')))
print(entrada)
