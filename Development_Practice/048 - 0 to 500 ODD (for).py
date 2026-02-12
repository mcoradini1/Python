#A PROGRAM TO TAKE NUMBERS FROM 0 TO 500, ONLY CONSIDERING NUMBERS DIVIDED BY 3 AND ODD.
sum_test = 0
count_test = 0
for c in range (0,501):
    if c%2 != 0 and c%3 == 0:
        sum_test = sum_test + c
        count_test = count_test + 1  #count_test+= 1
        print(sum_test, end=' ')
print('\n')
print(count_test)
