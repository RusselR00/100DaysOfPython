# Exercise 32:Sort 3 Integers
#  (Solved—19 Lines)
#  Create a program that reads three integers from the user and displays them in sorted
#  order (from smallest to largest). Use the min and max functions to find the smallest
#  and largest values. The middle value can be found by computing the sum of all three
#  values, and then subtracting the minimum value and the maximum value.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)
middle = num1 + num2 + num3 - minimum - maximum
print(f"The sorted numbers are: {minimum}, {middle}, {maximum}")
