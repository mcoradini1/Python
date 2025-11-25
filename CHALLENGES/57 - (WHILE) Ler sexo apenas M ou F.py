sexo = 'M'
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Qual o sexo do paciente? (M/F) ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('Resposta invalida tente novamente.\n')
        sexo = str(input('Qual o sexo do paciente? (M/F) ')).upper()



