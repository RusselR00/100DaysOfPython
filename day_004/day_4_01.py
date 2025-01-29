#  Exercise 21:Area of aTriangle
#  (13 Lines)
#  The area of a triangle can be computed using the following formula, where b is the
#  length of the base of the triangle, and h is its height:
#  area = b× h
#  2
#  Write a program that allows the user to enter values for b and h. The program
#  shouldthencomputeanddisplaytheareaofatrianglewithbaselengthbandheighth

b =float(input("Enter the length of the base:"))
h =float(input("Enter the height of the triangle from the base:"))

area = 0.5*b*h

print("area of the triangle :",area)