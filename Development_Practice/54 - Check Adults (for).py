import datetime
today = datetime.date.today().year
adult = 0
for c in range (1,8):
    year = int(input('Type the year of birthday of the {} person '.format(c)))
    if today - year >= 18:
        adult += 1
print('In this list we have: \n{} Adult(s) (18+)\n{} Underage(s) (18-)'.format(adult, 7 - adult))