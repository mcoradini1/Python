#ADDING ELEMENTS -------------------------------------------------------------------------------------------------------

people = {'name' : 'Gustavo', 'sex': 'M', 'age': 22}
people['weight'] = 98.5 #ADD A NEW ELEMENT
print(f'{people['name']} is {people['age']} years old')

#FOR EXAMPLES ----------------------------------------------------------------------------------------------------------
# (KEYS) ---------------------------------------------------------------------------------------------------------------
for k in people.keys(): #FOR EACH KEY IT WILL SHOW
    print(k)

# (ITEMS) SIMILAR TO ENUMERATE -----------------------------------------------------------------------------------------
for k, v in people.items(): #WE DON'T HAVE ENUMERATE FOR DICTIONARIES, WE SE LIKE THIS
    print(f'{k} and {v}')

#COPY WITHOUT BONDS (dictionary.copy()) --------------------------------------------------------------------------------
    estado = dict()
    brazil = list()
    for c in range(0, 3):
        estado['uf'] = str(input('Entre a sigla '))
        estado['sigla'] = str(input('Entre o estado '))

    brazil.append(estado.copy()) #THIS IS THE METHOD TO COPY DICTIONARIES
    print(brazil) #THIS WAY WOULD SHOW THE TRADITIONAL FORM

#COPY WRONG WAYS IN DICTIONARIES ---------------------------------------------------------------------------------------
    brazil.append(estado) #THIS WAY WOULD GENERATE A BOND BETWEEN THEM, MAKING THE 3 OF THEM THE SAME.
    brazil.append(estado[:]) #THIS WA DOES NOT WORK, BECAUSE IT'S USED ONLY FOR LISTS


#A BETTER WAY TO SHOW THE RESULTS IN THIS SITUATION

for e in brazil: #IT WILL TAKE EACH VALUE INSIDE THE LIST
    for k, v in e.items(): #FOR EACH VALUE INSIDE THE LIST, IT WILL TAKE EACH KEY AND VALUE FROM THE DICTIONARY
        print(f'The key {k} has the value of {v}.')
