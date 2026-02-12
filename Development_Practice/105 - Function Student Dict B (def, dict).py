# ADD OPTIONAL SITUATION (BAD, GOOD, MEDIUM, ALRIGHT EXCELLENT) AND DOCSTRING

def student_grades(* n, sit=False):
    r = dict ()
    r['total'] = len(n)
    r['higher'] = max(n)
    r['lower'] = min(n)
    r['average'] = sum(n)/len(n)
    if sit:
        if r['average'] >= 9:
            r['situation'] = 'EXCELLENT'
        elif r['average'] >= 7:
            r['situation'] = 'GOOD'
        elif r['average'] >= 5:
            r['situation'] = 'OK'
        elif r['average'] >= 3:
            r['situation'] = 'BAD'
        else:
            r['situation'] = 'VERY BAD'
    return r

print(student_grades(10,8,7,9,10,8, sit=True))