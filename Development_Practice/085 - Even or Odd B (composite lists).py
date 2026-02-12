#PROGRAM AN ALGORITHM TO READ 7 NUMBERS TELL IF THEY ARE EVEN OR ODD, STORE THEM AND IN THE END SHOW ALL EVENS AND ODDS
#IN NUMERICAL ORDER CRESCENT

list_general = [[], []]

for c in range (1,8):
    a = int(input(f'Type {c} number '))
    if a % 2 == 0:
        list_general[0].append(a)
    else:
        list_general[1].append(a)

list_general[0].sort()
list_general[1].sort()

print(f'EVENS {list_general[0]} \nODDS {list_general[1]}')