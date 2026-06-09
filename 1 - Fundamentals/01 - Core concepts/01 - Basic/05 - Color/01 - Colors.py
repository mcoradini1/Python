"""
It's important to note that when you start the text color, It will affect not only one print, but all until you
return to the default state.

\033[style:text:background m] - ANSI system

----- styles -----
0 - None, 1 Bold, 4 Underline, 7 Negative

----- text and background ----
30 to 37 (white, red, green, yellow, blue, purple,sky blue, grey)

"""

print('\033[1:31:43mStarting the cycle') #I start here, everything in the program will be like that until I close the cycle
print('\nPart of the cycle')
print('\033[mClosing the cycle...') #closing the cycle here...