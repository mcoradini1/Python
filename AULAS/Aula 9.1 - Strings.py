frase = 'Curso em Video Python'
dividido = frase.split() #dividi a frase em uma lista, onde os espacos determinam cada elemento...
juntar = '-'.join(dividido)
print(juntar)
print(dividido[2])
print(dividido[2][3]) #Vai pegar o elemento 2 (comeca do 0) da lista, neste caso Video , e a 3 elemento dessa palavra
print(len(frase)) #contar o tamahno da frase
# .strip() para tirar espaco inicio e fim

#.upper() por em maiusculo

