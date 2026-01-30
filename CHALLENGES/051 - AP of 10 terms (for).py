#PROGRAM AN ALGORITHM TO DO THE 10 FIRST TERMS OF AN ARITHMETIC PROGRESSION


t = int(input('First term: '))
r = int(input('Rate: '))

term_10th = t + (11 - 1) * r #THIS IS THE EQUATION TO FIND THE 10TH TERM
for c in range (t, term_10th, r): #REMEMBER: First term (starts), last term (end), rate (how much will sum)
    print(c, end = ' -> ')
print('FINISHED')


