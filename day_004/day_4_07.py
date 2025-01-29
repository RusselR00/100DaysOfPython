# Exercise 27:BodyMassIndex

# (14 Lines)

# Write a program that computes the body mass index (BMI) of an individual. Your

# program should begin by reading a height and weight from the user. Then it should  use one of the following two formulas to compute the BMI before displaying it. If

# you read the height in inches and the weight in pounds then body mass index is

# computed using the following formula:

# BMI = weight

# height × height × 703.

# If you read the height in meters and the weight in kilograms then body mass index

# is computed using this slightly simpler formula:

# BMI = weight

# height × height .
units = input("Enter units ('metric' or 'imperial'): ").lower()

if units not in ["metric", "imperial"]:
    print("Invalid units. Please enter 'metric' or 'imperial'.")
    exit()

if units == "metric":
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
elif units == "imperial":
    height = float(input("Enter height in inches: "))
    weight = float(input("Enter weight in pounds: "))

if units == "metric":
    bmi = weight / (height * height)
elif units == "imperial":
    bmi = (weight / (height * height)) * 703

print(f"BMI: {bmi:.2f}") 