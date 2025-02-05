#  Exercise 49:Richter Scale
#  (30 Lines)
#  The following table contains earthquake magnitude ranges on the Richter scale and
#  their descriptors:
#  Magnitude Descriptor
#  Less than 2.0 Micro
#  2.0tolessthan3.0 Veryminor
#  3.0tolessthan4.0 Minor
#  4.0tolessthan5.0 Light
#  5.0tolessthan6.0 Moderate
#  6.0tolessthan7.0 Strong
#  7.0tolessthan8.0 Major
#  8.0 to less than 10.0 Great
#  10.0 or more Meteoric
#  Write aprogramthatreadsamagnitudefromtheuseranddisplaystheappropriate
#  descriptor as part of a meaningful message. For example, if the user enters 5.5 then
#  your program should indicate that a magnitude 5.5 earthquake is considered to be a
#  moderate earthquake

magnitude = float(input("Enter the earthquake magnitude: "))

if magnitude < 2.0:
    descriptor = "Micro"
elif magnitude < 3.0:
    descriptor = "Very minor"
elif magnitude < 4.0:
    descriptor = "Minor"
elif magnitude < 5.0:
    descriptor = "Light"
elif magnitude < 6.0:
    descriptor = "Moderate"
elif magnitude < 7.0:
    descriptor = "Strong"
elif magnitude < 8.0:
    descriptor = "Major"
elif magnitude < 10.0:
    descriptor = "Great"
else:
    descriptor = "Meteoric"

print("A magnitude", magnitude, "earthquake is considered to be", descriptor, "earthquake.")