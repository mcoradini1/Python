expressao = str(input('Digite a expressao '))
parenteses = []
for paren in expressao:
    if paren == '(':
        parenteses.append('(')
    elif paren == ')':
        if len(expressao) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
print(f' -> {parenteses}')

if len(parenteses) == 0:
    print('expressao no grau!')
else:
    print('vai resolver esse pepino')