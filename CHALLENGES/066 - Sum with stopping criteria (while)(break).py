#MAKE A SUM PROGRAM like 065 THAT WILL STOP WHEN I PRESS 999 (using break). NOT CONSIDERING 999 AS SUM...

n_count = 0
n_sum = 0
n = 0
while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    n_count+=1
    n_sum = n_sum + n

print ('The sum is {}\nYou typed {} numbers'.format(n_sum,n_count-1))

