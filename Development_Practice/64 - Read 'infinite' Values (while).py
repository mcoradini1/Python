#A PROGRAM TO READ VALUES UNTIL I ASK IT TO STOP:
#SHOW, THE HIGHER, LOWER AND AVERAGE

n_major = 0
n_minor = 0
n_sum = 0
n_count = 0
n = 0
stop = 'Y'

while stop == 'Y':
    n_count+=1
    n = int(input('Type the {} number: '.format(n_count)))
    n_sum = n_sum + n
    if n > n_major:
        n_major = n
    if n_minor == 0:
        n_minor = n
    if n_minor > n:
        n_minor = n
    #print(n_sum, end =' ')

    stop = str(input('\n\nWould you like to continue? (Y/N): ')).upper()
print('\nHigher = {}\nLower = {}\nAverage = {}'.format(n_major, n_minor, n_sum / n_count))