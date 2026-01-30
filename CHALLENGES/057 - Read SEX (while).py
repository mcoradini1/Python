sex = str(input('What is the patient sex? (M/F) ')).upper()
while sex != 'M' and sex != 'F':
    print('Invalid answer.\n')
    sex = str(input('What is the patient sex? (M/F) ')).upper()
print(f'Thank you for using this program. The patient is {sex}')





