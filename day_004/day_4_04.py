# Exercise 24:Units ofTime
#  (22 Lines)
#  Create a program that reads a duration from the user as a number of days, hours,
#  minutes, and seconds. Compute and display the total number of seconds represented
#  by this duration


days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

print(f"Total seconds: {total_seconds}") 