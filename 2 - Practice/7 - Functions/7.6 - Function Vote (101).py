# ======================================================================================================================
# CHALLENGE 101: Function Vote
# ======================================================================================================================

"""
Challenge: 7.6 - Function Vote (101)
Category: 7 - Collections
Concepts Used:


Tags: import datetime, date.today().year, if, elif, else
Status: ✔️ Completed
"""

def vote_first(year):
    import datetime
    age = datetime.date.today().year - year
    if age > 65:
        return f'With {age} vote is OPTIONAL'

    elif age < 18:
        return f'With {age} vote is DENIED'

    else:
        return f'With {age} Vote is MANDATORY'

print(vote_first(1996))
print(vote_first(2000))
print(vote_first(2010))
print(vote_first(2018))

#-----------------------------------------------------------------------------------------------------------------------

def vote_second(year):
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

enter_year = vote_second(int(input('Type the year that you were born ')))
print(enter_year)

