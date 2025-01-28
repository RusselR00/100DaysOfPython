#  Exercise 19:Free Fall
#  (Solved—16 Lines)
#  Create a program that determines how quickly an object is traveling when it hits the
#  ground.Theuserwillentertheheightfromwhichtheobjectisdroppedinmeters(m).
#  Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
#  due to gravity is 9.8m/s2. You can use the formula vf = v2
#  i + 2ad to compute the
#  f inal speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known

import math

gravity = 9.8

height = float(input("Enter the height from which the object is dropped (in meters): "))

final_speed = math.sqrt(2 * gravity * height)

print(f"The final speed of the object when it hits the ground is: {final_speed:.2f} m/s")
