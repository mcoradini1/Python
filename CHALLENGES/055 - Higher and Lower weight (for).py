#PROGRAM TO READ 5 WEIGHTS AND TELL THE HIGHER AND LOWER

higher = 0
lower = 0
for c in range (1, 6):
    weight = float(input('Type the weight of the {} participant: '.format(c)))
    if weight > higher:
        higher = weight
    if lower == 0 or lower > weight:
        lower = weight
print('\nHigher weight -> {:.2f}\nLower peso -> {:.2f}'.format(higher, lower))