# Create a program that reads the length and width 
# of a farmer’s field from the user in
 #feet. Display the area of the field in acres.
w = float(input("Enter the width of the room in feets: \n"))
l = float(input("Enter the length of the room in feets: \n"))
a=  (w*l)/43560
print("Area of the room is",a,"acres")
