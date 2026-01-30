#A PEOPLE REGISTER PROGRAM THAT WILL RECEIVE AGE, SEX AND WILL PROVIDE:
#PEOPLE 18+, HOW MANY MENS ARE REGISTERED, WOMEN LOWER 20

age_18 = 0
men = 0
women_20 = 0

while True:
    print('-'*60)
    age = int(input('Type the age '))
    sex = int(input('[1] Male\n[2] Female\n '))
    print('-'*60)
    if age >= 18:
        age_18+=1
    if sex == 1:
        men+=1
    if age <= 20 and sex == 2:
        women_20 += 1
    while True:
        continue_yn = str(input('Would you like to continue? Y/N\n')).upper().strip()
        if continue_yn == 'N' or continue_yn == 'Y':
            break
    if continue_yn == 'N':
        break
print(f'{age_18} People above 18\n{men} Men(s) registered\n{women_20} Women lower 20 years old')


