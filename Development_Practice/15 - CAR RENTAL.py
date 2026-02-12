#CAR RENT PER DAY (60 POUNDS). PER MILE (0.65 CENTS)

kmd = float(input('How many miles expected? '))
diad = float(input('How many days? ') )
km = 0.65
dia = 60

print('With {} miles and {} days'.format(kmd,diad))

print('The total value to pay will be £ {:.2f}'.format((km*kmd)+(diad*dia)))


