#MAKE A SUM PROGRAM THAT WILL STOP WHEN I PRESS 999. NOT CONSIDERING 999 AS SUM...

n_count = 0
n_sum = 0
n = 0
while n != 999:
    n = int(input('Type a number: '))
    n_count+=1
    if n != 999:
        n_sum = n_sum + n
print ('The sum is {}\nYou typed {} numbers'.format(n_sum,n_count-1))

