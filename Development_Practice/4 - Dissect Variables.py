#CHALLENGE 4 - DISSECT VARIABLES WITH THE MOST COMMON METHODS.

n = str(input('Type anything: '))
print('The primitive value of this is ', type(n))
print('Is it only spaces ? ',n.isspace())
print('Is it a number? ', n.isnumeric())
print('Is it alphanumeric? ', n.isalnum())
print('Is it all uppercase? ', n.isupper())
print('Is it all lowercase? ', n.islower())
print('Is it normal format? ', n.istitle())
