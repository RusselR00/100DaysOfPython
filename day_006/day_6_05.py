
#  Exercise 40:NamethatTriangle
#  (Solved—20 Lines)
#  Atriangle can be classified based on the lengths of its sides as equilateral, isosceles
#  or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
#  triangle has two sides that are the same length, and a third side that is a different
#  length. If all of the sides have different lengths then the triangle is scalene.
#  Write a program that reads the lengths of 3 sides of a triangle from the user.
#  Display a message indicating the type of the triangle

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the type of triangle
if side1 == side2 == side3:
    triangle_type = "equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "isosceles"
else:
    triangle_type = "scalene"

# Display the result
print(f"The triangle is {triangle_type}.")