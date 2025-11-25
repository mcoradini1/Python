#ler varios valores e perguntar se quer continuar ou parar, no final dar media, maior e menor

n_maior = 0
n_menor = 0
n_soma = 0
n_count = 0
n = 0
stop = 'S'

while stop == 'S':
    n_count+=1
    n = int(input('Digite o {} numero '.format(n_count)))
    n_soma = n_soma + n
    if n > n_maior:
        n_maior = n
    if n_menor == 0:
        n_menor = n
    if n_menor > n:
        n_menor = n
    print(n_soma, end = ' ')
    stop = str(input('\n\nVoce gostaria de continuar? (S/N) ')).upper()
print('\nMaior = {}\nMenor = {}\nMedia = {}'.format(n_maior,n_menor,n_soma/n_count))