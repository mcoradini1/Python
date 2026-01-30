#CHECK STUDENT SITUATION ACCORDING TO 2 TESTS RESULTS.
#(LESS THAN 5 = FAILED) (BETWEEN 5 AND 6.9 = EXTRA TEST) (7+ APPROVED)

n1 = float(input('Type the first result: '))
n2 = float(input('Type the second result: '))

average = (n1 + n2) / 2
if average < 5: #if average >= 5 and average < 7: (USING AND)
    print('{} -> Student FAILED'.format(average))
elif average > 7:
    print('{} -> Student PASS'.format(average))
else:
    print('{} -> Student needs to do extra exam'.format(average))