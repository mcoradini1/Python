def vote(year):
    import datetime
    age = datetime.date.today().year - year
    if age > 65:
        f = f'With {age} vote is OPTIONAL'
        return f
    elif age < 18:
        f = f'With {age} vote is DENIED'
        return f
    else:
        f = f'With {age} Vote is MANDATORY'
        return f

enter_year = vote(int(input('Type the year that you were born ')))
print(enter_year)

