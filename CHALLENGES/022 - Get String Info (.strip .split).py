#PROGRAM TO RECEIVE AN NAME AND MAKE IT ALL UPPERCASE, LOWERCASE
#HOW MANY LETTERS, HOW MANY LETTERS FIRST NAME

name = str(input('Type a name: ')).strip() #.strip REMOVE WRONG SPACES BEFORE AND AFTER THE STRING
print('The name in UPPERCASE {}'.format(name.upper()))
print('The name in LOWERCASE {}'.format(name.lower()))
print('The name has {} letters'.format(len(name) - name.count(' ')))

#TWO DIFFERENT APPROACHES TO THE FIRST NAME LETTERS
print('Your first name has {} letters'.format(name.find(' '))) #IT WILL FIND THE FIRST SPACE AND GIVE THE NUMBER OF THAT

#THIS APPROACH USES SPLIT TO SEPARATE AN STRING INTO A LIST, THE TERM 0 IS THE FIRST TERM (FIRST NAME)
split_name = name.split()
print('Your first name is {} and it has {} letters'.format(split_name[0], len(split_name[0])))




