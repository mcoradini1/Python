#PROGRAM TO CALCULATE BMI

weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))
bmi = weight / (height ** 2)
print('Your BMI is:', bmi) #ANOTHER WAY TO SHOW

if bmi < 18.5:
    print('Lower -18.5')
elif 18.5 <= bmi < 25:
    print('Normal between 18.5 and 24.9')
elif 25 <= bmi < 30:
    print('Overweight between 25 and 30')
elif 30 <= bmi < 35:
    print('Obesity 1 between 30 and 35')
elif 35 <= bmi < 40:
    print('Obesity 2 between 35 and 40')
elif 40 <= bmi < 50:
    print('Obesity 3 between 40 and 50')
else:
    print('Obesity IV above 50')




