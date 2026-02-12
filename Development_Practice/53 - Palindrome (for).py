#A PROGRAM TO CHECK IF A WORD IS A PALINDROME (SAME READING BACKWARDS)
#SPECIAL CHARACTERS (.,!?) NOT CONSIDERED
#EXAMPLES TO CHECK: ''Doc note I dissent'' , ''Nurse I spy gypsies run''

p = input('Type the phrase? ').strip().upper()
words = p.split() #SPLIT INTO WORDS
words_join = ''.join(words) #JOIN IT WITHOUT SPACE ON '' I COULD ADD SPACE IN CASE I NEED IT SEPARATED
backwards = ''
for letters in range(len(words_join) - 1, -1, -1): #TO MAKE SURE I WILL START FROM THE LAST TERM, GOING DOWN TILL 0 (-1 NOT CONSIDER)
    backwards += words_join[letters]

print(words_join, backwards)

if backwards == words_join:
    print('IT IS PALINDROME')
else:
    print('IT IS NOT PALINDROME')

#CAN ALSO DO backwards = words_join[::-1] only that would make the word inverted

