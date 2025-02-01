# Exercise 37:NamethatShape
#  (Solved—31 Lines)
#  Write a program that determines the name of a shape from its number of sides. Read
#  the number of sides from the user and then report the appropriate name as part of
#  a meaningful message. Your program should support shapes with anywhere from 3
#  up to (and including) 10 sides. If a number of sides outside of this range is entered
#  then your program should display an appropriate error message

num_sides = int(input("Enter the number of sides of the shape (between 3 and 10): "))

if num_sides == 3:
    shape_name = "triangle"
elif num_sides == 4:
    shape_name = "quadrilateral"
elif num_sides == 5:
    shape_name = "pentagon"
elif num_sides == 6:
    shape_name = "hexagon"
elif num_sides == 7:
    shape_name = "heptagon"
elif num_sides == 8:
    shape_name = "octagon"
elif num_sides == 9:
    shape_name = "nonagon"
elif num_sides == 10:
    shape_name = "decagon"
else:
    shape_name = "Unknown shape. Number of sides must be between 3 and 10."
print(f"A shape with {num_sides} sides is a {shape_name}.")