#Escrva um programa que leia um valor em metros e exiba a conversao em cm e mm
m = int(input('Entre a medida em metros '))
print('Para centimetros {}cm\nPara millimetros {}mm'.format(m*100,m*1000))