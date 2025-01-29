#  Exercise 23:Area of aRegularPolygon
#  (Solved—14 Lines)
#  Apolygon is regular if its sides are all the same length and the angles between all of
#  the adjacent sides are equal. The area of a regular polygon can be computed using
#  the following formula, where s is the length of a side and n is the number of sidesarea =
#  n ×s2
#  4 ×tan π
#  n
#  Write a program that reads s and n from the user and then displays the area of a
#  regular polygon constructed from these values

import math

s = float(input("Enter the length of a side: "))
n = int(input("Enter the number of sides: "))

if n < 3:
    raise ValueError("The number of sides must be at least 3.")
if s <= 0:
    raise ValueError("The side length must be greater than 0.")

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of the regular polygon is: {area:.2f}")