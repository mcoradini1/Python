#NOTAS DO ALUNO EM PROVA (5 REPORVADO, 5 A 6.9 ERCUPOERACAO, 7 APROVADO)
n1 = float(input('Entre a primeira nota '))
n2 = float(input('Entre a segunda nota '))
media = (n1+n2)/2
if media >= 5 and media < 7:
#if 5 <= media < 7:     tambem poderia fazer assim... mais pratco e rapido
    print('Sua media foi {} voce esta de recuperacao'.format(media))
elif media > 7:
    print('Sua media foi {}. \nParabens voce foi Aprovado'.format(media))
else:
    print('Sua media foi {}, voce foi Reprovado'.format(media))