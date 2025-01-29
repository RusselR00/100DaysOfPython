#  Exercise 26:CurrentTime
#  (10 Lines)
#  Python includes a library of functions for working with time, including a function
#  called asctime in the time module. It reads the current time from the com
# puter’s internal clock and returns it in a human-readable format. Write a program
#  that displays the current time and date. Your program will not require any input from
#  the user.
import time

current_time = time.asctime()

print("Current time:", current_time)