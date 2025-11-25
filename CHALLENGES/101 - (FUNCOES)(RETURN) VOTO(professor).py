def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if ano > 65:
        return f'Com {idade} anos o voto e OPCIONAL'

    elif ano < 18:
        return f'Com {idade} anos o voto e NEGADO'

    else:
        return f'Com {idade} anos o voto e OBRIGATORIO'

print(voto(1996))
