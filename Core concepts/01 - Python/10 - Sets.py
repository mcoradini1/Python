#SETS ARE UNORDERED COLLECTIONS OF DISTINCT HASABLE OBJECTS
#SET (MUTABLE) AND FROZEN SET
#ALL NUMBERS WITHIN SETS ARE UNIQUE (DISTINCT)

id_set = set([1,2,3,4,5,6,7,8,9])
print(id_set)
id_set.add(9)
print(id_set)
id_set.remove(9)
print(id_set)

id_set_range = set(range(10))
print(id_set_range)
males = set([1,2,3,4,5])
print(males)
females = id_set_range - males
print(females)
print('-'*60)
print(males.symmetric_difference(females))


everyone = males | females  #union between sets
males.issubset(everyone)  #chck if everyone has everyone from males...

set_and = everyone & set([1,2,25,9]) # show the ones that they have in common only
print(set_and)

word = 'python is a great programming language'
letters = set(word)
print(len(letters))
print(letters)


#COPYING
#SHALLOW COPY

import copy
x = [1,[2]]
y = copy.copy(x)
z = copy.deepcopy(x)
print(y is z) #false


