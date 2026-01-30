#PROGRAM TO CHECK IF THERE IS SILVA IN A NAME TYPED
nome = str(input('Type your complete name: ')).strip()
print('Your name has Silva? {}'.format('silva' in nome.lower()))