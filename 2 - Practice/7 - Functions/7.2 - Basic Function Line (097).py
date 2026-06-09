# ======================================================================================================================
# CHALLENGE 97: Basic Function Line
# ======================================================================================================================

"""
Challenge: 7.2 - Basic Function Line (097)
Category: 7 - Collections
Concepts Used: def, len


Tags: def, len
Status: ✔️ Completed
"""

def write_line(name):
    a = len(name) + 2
    print('~'*a)
    print(f' {name}')
    print('~'*a)

write_line('Functions are cool')
write_line('01 - Python is cool')
