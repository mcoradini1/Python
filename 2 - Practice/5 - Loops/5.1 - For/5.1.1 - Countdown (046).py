# ======================================================================================================================
# CHALLENGE 46: Countdown: Countdown and show a boom message.
# ======================================================================================================================

"""
Challenge: 5.1.1 - Countdown (046)
Category: 5 - Loops
Concepts Used:
    - import time
    - for
    - range()
    - sleep()
    - print()



Tags: import time, for, range(), sleep(), print()
Status: ✔️ Completed
"""

import time
for c in range(10, -1, -1):
    time.sleep(0.5)
    print(c)
print('Boooooooooooom!')