phrase = 'Python as a prOgramming language'
print(phrase[3]) #Get only the third element in this case 'T'
print(phrase[3:13]) #Get the 3rd element until the 13th (not considering 13th)
print(phrase[::2]) #no start. no ending, going 2 by 2
print(phrase.count('o')) #count the amounts of 'o' (Case sensitive)
print(phrase.upper().count('O')) #set everything to CAPS and then count O (Better way to work)
#.upper()[0] in this example I would just make the member 0 CAPITAL...

print(phrase.lower().count('o')) #set everything to lowercase... same as the previous example...
print(phrase.replace('Python', 'Android')) #replace text
print(phrase.find('Language')) #if this show -1 means that did not find...
print(phrase.find('language')) #here shows where language starts...
print(phrase.lower().find('language')) #smart way to do the two examples above

#To make the command works right to left we just add an 'r' in front of the command

#print('Test {}'.format(variable.find('A')+1))
#print('Test {}'.format(variable.rfind('A')+1))

#that will show the first A, from left and them from right...

print("""\n\nonly a test ddsfdsfsdfsdfdsf
dfsdfdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfds
fdfsdfsdfdsfsdfsdfsdfsdfsdfsdfsdfsd """) #If I use 3 """ I can make texts like that