#Create a function to generate random passwords
from random import choice



def password(length):
    pw = str()
    letters = 'abcdefghijklmnopqrstuvxzy' + '0123456789'
    for i in range(length):
        pw = pw + choice(letters)
    return pw

print(password(10))


#could use the library bellow to be easier
# import string  #letters = string.ascii_letters + string.digits + string.punctuation