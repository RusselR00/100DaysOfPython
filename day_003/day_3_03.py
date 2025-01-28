# Exercise 18:VolumeofaCylinder
#  (15 Lines)
#  The volume of a cylinder can be computed by multiplying the area of its circular
#  base by its height. Write a program that reads the radius of the cylinder, along with
#  its height, from the user and computes its volume. Display the result rounded to one
#  decimal place.
# import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

base_area = math.pi * radius ** 2

volume = base_area * height

print(f"The volume of the cylinder is: {volume:.1f}")
