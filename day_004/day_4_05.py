# Exercise 25:Units ofTime(Again)
#  (Solved—24 Lines)
#  In this exercise you will reverse the process described in the previous exercise.
#  Develop a program that begins by reading a number of seconds from the user.
#  Then your program should display the equivalent amount of time in the form
#  D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec
# onds respectively. The hours, minutes and seconds should all be formatted so that
#  they occupy exactly two digits, with a leading 0 displayed if necessary

total_seconds = int(input("Enter the number of seconds: "))

days = total_seconds // (24 * 60 * 60)
total_seconds %= 24 * 60 * 60
hours = total_seconds // (60 * 60)
total_seconds %= 60 * 60
minutes = total_seconds // 60
seconds = total_seconds % 60

formatted_time = f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}"
print(f"Equivalent time: {formatted_time}")