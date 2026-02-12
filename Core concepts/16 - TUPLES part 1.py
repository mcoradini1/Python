#COMPOSITE VARIABLES THAT CANNOT BE CHANGED

Snack = ('Hamburguer', 'Juice', 'Pizza', 'Pudim')
print(Snack)
print(Snack[3]) #The third term is PUDIM, because HAMBURGUER is the term 0
print(Snack[1:3]) #Cutting not considering the last term, starts on Juice and finishes on Pizza)

print('\n\n')

for food in Snack:
    print(f'I will eat {food}')
print('I ate to much!')


print('\n\n')


for cont in range(0, len(Snack)):
    print(Snack[cont])


print('\n\n')

for pos, food in enumerate(Snack): #when use enumerate i have to use 2 variables here...
#first term pos is position, and food is the content of the variable...
    print(f'I will eat {food} in the position {pos}')

print('\n\n')

print(sorted(Snack)) #To put it in alphabetic order