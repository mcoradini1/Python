#ALGORITHM TO READ 6 VALUES AND SHOW HOW MANY EVEN, ODD AND THE SUM OF EVENS. USING ONLY 2 SUPPORT VARIABLES

sum_even = 0
count_odd = 0
for c in range(1, 7):
    n = int(input('Type the {} value '.format(c)))
    if n%2 == 0:
        sum_even = sum_even + n
    else:
        count_odd = count_odd + 1

print('\n\n{} EVENS \n{} ODDS \n{} SUM OF EVENS'.format(6 - count_odd, count_odd, sum_even))
