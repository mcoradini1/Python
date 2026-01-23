phrase = 'Python as a programming language'
divided = phrase.split()  # Divide the variable phrase into a list where spaces determine each element
join = '-'.join(divided) # Join the list, in this case using hifen as space.
print(join)
print(divided[2]) #show the second element in the list divided (starts from element 0, this will be 'A')
print(divided[3])
print(divided)  #print the whole list...
print(len(phrase)) #counts the size of characters of the variable

# .strip() cuts spaces on the beggining and ending of variables
#.upper() set everything to CAPITALCASE

