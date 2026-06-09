# ==========================================================================================================
# CHALLENGE 26: PHRASE DISSECT: How many 'A' and first/last position.
# ==========================================================================================================

"""
Challenge: 2.5 - Phrase Dissect (26)
Category: 2 - Strings and Text Processing
Concepts Used:
    - .strip()
    - .upper()
    - .find
    - .rfind
    - .format
    - print()


Tags: .strip(), .upper(), .find(), .rfind(), .format(), print()
Status: ✔️ Completed
"""


phrase = str(input('Type a phrase ')).strip().upper()

#phrase = 'The letter A is amazing, awesome and great'.upper() <- THIS IS JUST FOR FAST TESTING


print('This phrase has {} letters (A)'.format(phrase.count('A')))
print('The first letter (A) happens at {}'.format(phrase.find('A') + 1))
print('The last letter (A) happens at {}'.format(phrase.rfind('A') + 1))








