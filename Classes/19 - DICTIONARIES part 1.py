#HERE I HAVE GOT ALPHABETIC INDEXES (Can set names instead of numbers)
# {} determine the dictionaries

#INITIAL EXAMPLE -------------------------------------------------------------------------------------------------------
#TWO WAYS TO MAKE AN EMPTY DICTIONARY
#data = {}
#movie = dict()

data = {'name': 'Pedro', 'age':25} #THAT'S A DICTIONARY WITH 2 TERMS; TERM 1: NAMED AS NAME, TERM2: AGE

#PRINT DATA ------------------------------------------------------------------------------------------------------------
print(data['name']) # PEDRO
print(data['age']) #25

#ADD INFORMATION -------------------------------------------------------------------------------------------------------
data['sex'] = 'Male' #HERE I DON'T USE APPEND

#DELETE ----------------------------------------------------------------------------------------------------------------
del data['age']

#IMPORTANT COMMANDS IN DICTIONARIES ------------------------------------------------------------------------------------
print(data.values()) #SHOWS ONLY THE VALUES (PEDRO, 25, MALE)
print(data.keys()) #SHOW ONLY THE KEYS (NAME, AGE, SEX)
print(data.items) #SHOWS THE WHOLE DICTIONARY (VALUES AND KEYS)


#EXAMPLE ---------------------------------------------------------------------------------------------------------------
for k,v in data.items():
    print(f'The key is {k} and the value is {v}')
    #IT WILL SHOW NAME (PEDRO) AGE (25) SEX (MALE), FOLLOWING ALL IN THIS DICTIONARY


#JOINING LISTS WITH DICTIONARIES ---------------------------------------------------------------------------------------
#IMAGINE LISTS INSIDE THE DICTIONARY
age_list = [30,12,25,35,40]
dictionary_people = {'age':age_list}

