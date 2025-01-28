import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

base_area = math.pi * radius ** 2

volume = base_area * height

print(f"The volume of the cylinder is: {volume:.1f}")
