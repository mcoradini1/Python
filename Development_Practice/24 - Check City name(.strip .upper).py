#PROGRAM TO CHECK IF A CITY STARTS WITH THE NAME 'SANTO'
city = str(input('Type a city name? ')).strip() #CUT THE SPACES
print(city[:5].upper() == 'SANTO')

#[:5] IT WILL TAKE FROM 0 TO 4 (5 FIRST LETTERS)
