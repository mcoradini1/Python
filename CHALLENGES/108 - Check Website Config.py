#Check if the website pudim is available
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br/')
except:
    print('NOT accessible')
else:
    print('OK')

