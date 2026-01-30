t = int(input('Enter the first term '))
r = int(input('Enter the ratio '))

result = t
term_10th=0
while not term_10th == 11:
    print(result, end=' -> ')
    term_10th+=1
    result = result + r
print('END')