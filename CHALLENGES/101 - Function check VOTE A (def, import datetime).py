def vote(ano):
    import datetime
    age = datetime.date.today().year - ano
    if age > 65:
        return f'With {age} vote is OPTIONAL'

    elif age < 18:
        return f'With {age} vote is DENIED'

    else:
        return f'With {age} Vote is MANDATORY'

print(vote(1996))
print(vote(2000))
print(vote(2010))
print(vote(2018))
