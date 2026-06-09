# ===============================================================================================================
# CHALLENGE 25: Name Checker
# ===============================================================================================================

"""
Challenge: 2.4 - Name Checker (025)
Category: 2 - Strings and Text Processing
Concepts Used:
    - str()
    - lower()
    - .strip()
    - print()
    -.format
    - in

Tags: print(), str(), .upper(), .strip(), .format(), in
Status: ✔️ Completed

#PROGRAM TO CHECK IF THERE IS SILVA IN A NAME TYPED
"""


nome = str(input('Type your complete name: ')).strip()
print('Your name has Silva? {}'.format('silva' in nome.lower()))