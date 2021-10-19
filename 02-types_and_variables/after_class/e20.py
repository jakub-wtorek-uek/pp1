# 20.	Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg.
# The user enters the data from the keyboard. Find the formula on the Internet for calculating BMI.
# Then, using your program, check that you have the correct weight. Sample result:
# Enter your height in cm: ...
# Enter your weight in kg: ...
# BMI index: ...

height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

bmi_index = round(weight / (height**2) * 10000, 1)

print(f"BMI index: {bmi_index}")
