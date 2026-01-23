n1 = int(input('Type a value : '))
n2 = int(input('Type another value : '))
m = n1/n2
print('\nThe division: \n{:.3f}' .format(m), end=' >>> ')

#the end command will put the down line in front of the up line, everything inside it will be used instead of a paragraph.
#:.3f To consider 3 variables after comma.
#\n to break the line

print('{} / {}'.format(n1, n2))

print('\nHere some types of format for variables:')
name = ''
age = 18
name = 'Jose'
age = 33
salary = 1256.365484
print(f'{name} is {age} and his salary is {salary:.2f}\n') #.2f to consider only 2 decimals after the comma
print(f'{name:-^20}') #Centered in the middle of 20 ^
print(f'{name:20}') #20 spaces in front
print(f'{name:^20}') #20 spaces but centered
print(f'{name:-<20}') #20 instead of spaces hifen
print(f'{name:->20}') #20 instead of spaces hifen

