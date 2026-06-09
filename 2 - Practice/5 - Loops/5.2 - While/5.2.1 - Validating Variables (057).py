# ======================================================================================================================
# CHALLENGE 57: Validating Variables: Validate the SEX  variable though a while loop
# ======================================================================================================================

"""
Challenge: 5.2.1 - Validating Variables (057)
Category: 5 - Loops
Concepts Used:
    - while
    - .upper()


Tags: while, .upper()
Status: ✔️ Completed
"""

sex = str(input('What is the patient sex? (M/F) ')).upper()
while sex != 'M' and sex != 'F':
    print('Invalid answer.\n')
    sex = str(input('What is the patient sex? (M/F) ')).upper()
print(f'Thank you for using this program. The patient is {sex}')





