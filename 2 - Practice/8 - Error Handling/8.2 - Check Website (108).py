# ======================================================================================================================
# CHALLENGE 108: Check Website
# ======================================================================================================================

"""
Challenge: 8.2 - Check Website (108)
Category: 8 - Error Handling
Concepts Used:


Tags: import urllib.request, try, except, else
Status: ✔️ Completed
"""

#Check if the website pudim is available
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br/')
except:
    print('NOT accessible')
else:
    print('OK')

