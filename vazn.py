vazn = int(input())
ghad = float(input())

BMI = round((vazn / (ghad**2)),2)
print(BMI)
if BMI < 18.5:
    print('Underweight')

elif  18.5 <= BMI < 25:
    print('Normal')

elif  25 <= BMI < 30:
    print('Overweight')

else:
    print('Obese')