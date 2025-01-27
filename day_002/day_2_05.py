# Exercise 15:Distance Units
#  (20 Lines)
#  In this exercise, you will create a program that begins by reading a measurement
#  in feet from the user. Then your program should display the equivalent distance in
#  inches, yards and miles. Use the Internet to look up the necessary conversion factors
#  if you don’t have them memorized
feet = float(input("Enter the distance in feet: "))

fti = 12  
fty = 1 / 3
ftm = 1 / 5280
inches = feet * fti
yards = feet * fty
miles = feet * ftm

print(f"The equivalent distance is:")
print(f"{inches:.2f} inches")
print(f"{yards:.2f} yards")
print(f"{miles:.6f} miles")
