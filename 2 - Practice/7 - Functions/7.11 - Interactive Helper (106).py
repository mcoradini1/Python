# ======================================================================================================================
# CHALLENGE 106: Interactive Helper
# ======================================================================================================================

"""
Challenge: 7.11 - Interactive Helper (106)
Category: 7 - Collections
Concepts Used:


Tags: help(), len()
Status: ✔️ Completed
"""

c = (
    '\033[m',               #0 - no color
    '\033[30;41m',          #1 - red
    '\033[30;42m',          #2 - green
    '\033[30;43m',          #3 - yellow
    '\033[30;44m',          #4  - blue
    '\033[30;45m',          #5 - purple
    '\033[7;30m',           #6 - white
)


def help_py(word):
    title_program(f'Accessing the manual...', color=5)
    print(c[0])
    print(c[6], end='')
    help(word)
    print(c[0], end='')


def title_program(msg, color=2):
   size = len(msg) + 6
   print(f'{c[color]}-'*size)
   print(f'   {msg}')
   print(f'{c[color]}-'*size)



while True:
    title_program('-- Help SystemPy --')
    help_command = str(input(f'{c[0]} Library search -> '))
    if help_command.upper() == 'EXIT':
        break
    else:
        help_py(help_command)

print(f'{c[1]}BYE BYE')





