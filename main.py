print("Welcome to the BMI Calculator! ")
print("-------------------------------")
height=float(input("Please enter your height(m): "))
weight=int(input("please enter your weight(kg): "))
print()
bmi=round(weight/(height**2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight." )
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight." )
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight." )
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese." )
else:
    print(f"Your BMI is {bmi}, you are clinically obese." )
print("-------------------------------")
print("Thank you for using BMI Calculator! Stay Healthy!")