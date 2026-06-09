# ======================================================================================================================
# CHALLENGE 77: Only Vowels
# ======================================================================================================================

"""
Challenge: 6.1.6 - Only Vowels (077)
Category: 6 - Collections
Concepts Used:
    - tuples
    - for
    - if()
    - end = ''
    - .upper()
    - .lower()

Tags: tuples, for, if(), end = '', .upper(), .lower()
Status: ✔️ Completed
"""


#A PROGRAM THAT WILL GET THE VOWELS IN WORDS

words = ('potato', 'caramel', 'boot', 'tomato', 'cow', 'chicken', 'powder', 'bread', 'spring onion')

for p in words:
    print(f'\nIn the word {p.upper()} we have', end = ' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end =' ')
print('\n')

#INSIDE TUPLES EACH WORD IS A LIST OF LETTERS