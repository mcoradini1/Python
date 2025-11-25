n = input('Escreva algo numeros: ')
print(n.isnumeric(), 'para numeros')
# checar se e numero

m = input('Escreva algo letras: ')
print(m.isalpha(), 'pra letras')
#checar se e string

o = input('Escreva algo numero e letra: ')
print(o.isalnum(), 'para letras e numeros')
# se tem numero e string

p = input('Escreva algo em letras maiusculas: ')
print(p.isupper(), 'para letras maiusculas')
# para checar se todas letras sao maiusculas

q = input('Escreva algo em letras minusculas: ')
print(q.islower(), 'para letras minusculas')

# Ha outros testes como o isprint, isspace, se caso precisar so preciso testar
