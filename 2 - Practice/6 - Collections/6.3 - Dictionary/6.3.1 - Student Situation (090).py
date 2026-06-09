# ======================================================================================================================
# CHALLENGE 90: Student Situation
# ======================================================================================================================

"""
Challenge: 6.3.1 - Student Situation (090)
Category: 6 - Collections
Concepts Used:
    - dict
    - if()
    - elif()
    - else()
    - for
    -.items()

Tags: dict, if(), elif(), else(), for, .item()
Status: ✔️ Completed
"""

student = dict ()
student['name'] = str(input('Type the name: ')).title()
student['score'] = float(input(f'Type {student['name']}`s score: '))

if student['score'] >= 7:
    student['situation'] = 'APPROVED'
elif 5 >= student ['score'] < 7:
    student['situation'] = 'EXTRA TEST'
else:
    student['situation'] = 'FAIL'
print()
print('-'*30)

for k, c in student.items():
    print(f'{k} -> {c}')