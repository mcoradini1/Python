#PROGRAM TO READ A PHRASE AND GIVE ME
#HOW MANY 'A' ; ITS POSITION FIRST # ITS POSITION LAST

phrase = str(input('Type a phrase ')).strip().upper()

#phrase = 'The letter A is amazing, awesome and great'.upper() <- THIS IS JUST FOR FAST DEBUG


print('This phrase has {} letters (A)'.format(phrase.count('A')))
print('The first letter (A) happens at {}'.format(phrase.find('A') + 1))
print('The last letter (A) happens at {}'.format(phrase.rfind('A') + 1))








