# problem 12
#  The surface of the Earth is curved, and the distance between degrees of longitude
#  varieswithlatitude.Asaresult,findingthedistancebetweentwopointsonthesurface
#  of the Earth is more complicated than simply using the Pythagorean theorem.
#  Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
#  surface. The distance between these points, following the surface of the Earth, in
#  kilometers is:
#  distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
#  The value 6371.01 in the previous equation wasn’t selected at random. It is
#  the average radius of the Earth in kilometers.
#  Create a program that allows the user to enter the latitude and longitude of two
#  points on the Earth in degrees. Your program should display the distance between
#  the points, following the surface of the earth, in kilometers

import math

def calculate_distance(lat1, lon1, lat2, lon2):
    t1 = math.radians(lat1)
    g1 = math.radians(lon1)
    t2 = math.radians(lat2)
    g2 = math.radians(lon2)
    
    R = 6371.01
    
    distance = R * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
    
    return distance

print("Enter the coordinates of the first point:")
lat1 = float(input("Latitude (in degrees): "))
lon1 = float(input("Longitude (in degrees): "))

print("\nEnter the coordinates of the second point:")
lat2 = float(input("Latitude (in degrees): "))
lon2 = float(input("Longitude (in degrees): "))

distance = calculate_distance(lat1, lon1, lat2, lon2)


print(f"\nThe distance between the two points is {distance:.2f} km.")
