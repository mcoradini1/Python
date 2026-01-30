#PROGRAM AN ALGORITHM TO READ 7 NUMBERS TELL IF THEY ARE EVEN OR ODD, STORE THEM AND IN THE END SHOW ALL EVENS AND ODDS
#IN NUMERICAL ORDER CRESCENT

list_general = list ()
lista_even = list ()
lista_odd = list ()

for c in range (0,7):
    a = int(input(f'Type {c+1} number: '))
    if a % 2 == 0:
        lista_even.append(a)
        print('Even')
    else:
        lista_odd.append(a)
        print('Odd')
lista_even.sort()
lista_odd.sort()
list_general.append(lista_even[:])
list_general.append(lista_odd[:])


print(f'EVENS {list_general[0]} \nODDS {list_general[1]}')