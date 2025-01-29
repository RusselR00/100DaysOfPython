#  Exercise 22:Area of aTriangle (Again)
#  (16 Lines)
#  In the previous exercise you created a program that computed the area of a triangle
#  when the length of its base and its height were known. It is also possible to compute
#  the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
#  be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
#  can be calculated using the following formula:
#  area = 
# s ×(s −s1)×(s −s2)×(s −s3)
#  Develop a program that reads the lengths of the sides of a triangle from the user and
#  displays its area

s1 = float(input("Enter the length of first side"))
s2 = float(input("Enter the length of second side"))
s3 = float(input("Enter the length of third side"))

s = (s1+s2+s3)*0.5

area = (s*(s-s1)*(s-s2)*(s-s3))**0.5

print("area of the triangle is :",area)