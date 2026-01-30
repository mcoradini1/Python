#PROGRAM TO RECEIVE 5 VALUES, TELL ME THE HIGHER, LOWER AND SHOW THEM IN A LIST WITH THE POSITION THAT WERE TYPE

list_values = list()
for count in range(0, 5):
    list_values.append(int(input('Type a number: ')))
print('-'*60)
print(f'The highest is {max(list_values)} and appeared at position  {list_values.index(max(list_values))+1}')
print(f'The lower is {min(list_values)} and appeared at position  {list_values.index(min(list_values))+1}')
print('-'*60)
for c, c1 in enumerate(list_values):
    print(f'The term {c} is number {c1}')


