#PROGRAM TO READ SPEED (IF ABOVE 60 miles it's fined, 7 pounds per mile above)

speed = float(input('Type the speed? '))
if speed > 80:
    fine = (speed - 80) * 7
    print('You got fined in {:.2f} £'.format(fine))
else:
    print('You are alright, please keep your travel.')
print('\n\nHave a good day! ')