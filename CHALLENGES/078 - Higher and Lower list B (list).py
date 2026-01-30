#PROGRAM TO RECEIVE 5 VALUES, TELL ME THE HIGHER, LOWER AND SHOW THEM IN A LIST WITH THE POSITION THAT WERE TYPE

list_numbers = []
higher_number = 0
lower_number = 0
for c in range(0,5):
    list_numbers.append(int(input(f'Type a number for the position {c} ')))
    if c == 0:
        higher_number = lower_number = list_numbers[c]
    else:
        if higher_number < list_numbers[c]:
            higher_number = list_numbers[c]
        if lower_number > list_numbers[c]:
            lower_number = list_numbers[c]
print('-'*60)
print(f'The higher is {higher_number}, the lower is {lower_number}\n and the complete list is: {list_numbers}')
print('-'*60)
