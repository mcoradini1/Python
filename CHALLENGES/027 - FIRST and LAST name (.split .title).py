#A PROGRAM THAT READ A COMPLETE NAME AND ANSWER THE FIRST AND LAST NAME

name = str(input('Type your full name: ')).strip().title()
name_split = name.split()
print('Your First name is {}'.format(name_split[0]))
print('Your last name is {}'.format(name_split[len(name_split) - 1]))