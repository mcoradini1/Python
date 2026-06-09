"""
DICTIONARIES — Python Fundamentals

- Store key–value pairs
- Keys must be unique and immutable
- Values can repeat
- Mutable and ordered (Python 3.7+)
- Defined with {} or dict()
"""

# ---------------------------------------------------------
# CREATING DICTIONARIES
# ---------------------------------------------------------

data = {}                     # empty dictionary
movie = dict()                # empty dictionary

data = {'name': 'Pedro', 'age': 25}
print('name' in data)         # True (checks keys, not values)

# ---------------------------------------------------------
# ACCESSING VALUES
# ---------------------------------------------------------

print(data['name'])           # Pedro
print(data.get('age'))        # 25

# ---------------------------------------------------------
# ADDING & UPDATING
# ---------------------------------------------------------

data['sex'] = 'Male'          # add new key
data['age'] = 26              # update existing key

# ---------------------------------------------------------
# REMOVING
# ---------------------------------------------------------

del data['age']
data.pop('sex')
# data.popitem()              # removes last inserted pair

# ---------------------------------------------------------
# DICTIONARY VIEWS
# ---------------------------------------------------------

print(data.keys())            # dict_keys([...])
print(data.values())          # dict_values([...])
print(data.items())           # dict_items([...])

# ---------------------------------------------------------
# LOOPING THROUGH DICTIONARIES
# ---------------------------------------------------------

people = {'name': 'Gustavo', 'sex': 'M', 'age': 22}

for k in people.keys():
    print(k)

for v in people.values():
    print(v)

for k, v in people.items():
    print(f'{k} = {v}')

# ---------------------------------------------------------
# DICTIONARY INSIDE LIST (COPYING CORRECTLY)
# ---------------------------------------------------------

state = {}
brazil = []

for c in range(3):
    state['uf'] = input('UF: ')
    state['name'] = input('State: ')
    brazil.append(state.copy())     # correct copy

# WRONG: creates bonds (all entries become identical)
# brazil.append(state)

# ---------------------------------------------------------
# LOOPING THROUGH LIST OF DICTIONARIES
# ---------------------------------------------------------

for entry in brazil:
    for k, v in entry.items():
        print(f'{k}: {v}')

# ---------------------------------------------------------
# BUILDING A PEOPLE DATABASE
# ---------------------------------------------------------

database = []

dict_people = {'name': 'marlon', 'age': 31, 'weight': 90}
database.append(dict_people.copy())

dict_people = {'name': 'susana', 'age': 29, 'weight': 65}
database.append(dict_people.copy())

dict_people = {'name': 'anabela', 'age': 50, 'weight': 70}
database.append(dict_people.copy())

print(database[0]['weight'])
print(database)

for person in database:
    for key, value in person.items():
        print(f'{key} is {value}')
    print()

# ---------------------------------------------------------
# EXAMPLE 1: BEARS
# ---------------------------------------------------------

bears = {"Grizzly": "angry", "Brown": "friendly", "Polar": "friendly"}

for bear in bears:
    if bears[bear] == "friendly":
        print("Hello, " + bear + " bear!")
    else:
        print("odd")
