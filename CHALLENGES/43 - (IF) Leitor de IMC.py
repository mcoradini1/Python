#LEITOR D IMC
peso = float(input('Entre o peso em kg '))
altura = float(input('Entre a altura em m '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo -18.5')
elif 18.5 <= imc < 25:
    print('Normal entre 18.5 e 24.9')
elif 25 <= imc < 30:
    print('Sobrepeso entre 25 e 30')
elif 30 <= imc < 35:
    print('Obesidade 1 Entre 30 e 35')
elif 35 <= imc < 40:
    print('Obesidade 2 Entre 35 e 40')
elif 40 <= imc < 50:
    print('Obesidade 3 Entre 40 e 50')
else:
    print('Obesidade IV acima de 50')




