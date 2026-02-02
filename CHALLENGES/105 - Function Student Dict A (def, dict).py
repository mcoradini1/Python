#CREATE A FUNCTION FOR STUDENT GRADES, THAT WILL RECEIVE INFINITE GRADES FROM STUDENTS AND RETURN:
#HOW MANY GRADES WERE TYPED, HIGHER. LOWER, AVERAGE

def student_grades(* n):

    sun_grades = 0

    for a in n:
        sun_grades += a

    total = len(n)
    higher = max(n)
    lower = min(n)
    average = sun_grades/total


    dic_student = {'total': total, 'higher': higher, 'lower': lower, 'average': average}

    return dic_student

print(student_grades(1,2,3,4,5))