# ==========================================================================================================
# CHALLENGE 27: First and Last name: Read a full name and provide just the first and last
# ==========================================================================================================

"""
Challenge: 2.6 - First and Last name (27)
Category: 2 - Strings and Text Processing
Concepts Used:
    - .strip()
    - .split()
    - .title
    - .format
    - print()
    - len()

Tags: .strip(), .split(), .title, .format(), print(), len()
Status: ✔️ Completed
"""


name = str(input('Type your full name: ')).strip().title()
name_split = name.split()
print('Your First name is {}'.format(name_split[0]))
print('Your last name is {}'.format(name_split[len(name_split) - 1]))