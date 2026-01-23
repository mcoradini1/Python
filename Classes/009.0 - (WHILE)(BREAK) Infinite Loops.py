# while true: (It will continue until I break it)
n = s = m = 0

while True:
    n = int(input('Type a number '))
    if n == 999:
        break
    s += n
    m+=1
print('Numbers typed {} (disconsidering 999)'.format(m))
print(f'The sum is {s}')