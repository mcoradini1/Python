idade18 = 0
homens = 0
mulheres20 = 0

while True:
    print('-'*60)
    idade = int(input('Digite a sua idade '))
    sexo = int(input('[1] Masculino\n[2] Feminino\n '))
    print('-'*60)
    if idade >= 18:
        idade18+=1
    if sexo == 1:
        homens+=1
    if idade <= 20 and sexo == 2:
        mulheres20 += 1
    while True:
        continuar = str(input('Voce deseja continuar? S/N\n' )).upper().strip()
        if continuar == 'N' or continuar == 'S':
            break
    if continuar == 'N':
        break
print(f'{idade18} pessoas sao maiores de 18\nHa {homens} homens registrados\nHa {mulheres20} mulheres abaixo de 20 anos registradas')


