#  Exercise 38:MonthNametoNumberofDays
#  (Solved—18 Lines)
#  The length of a month varies from 28 to 31 days. In this exercise you will create
#  a program that reads the name of a month from the user as a string. Then your
#  program should display the number of days in that month. Display “28 or 29 days”
#  for February so that leap years are addressed


month = input("Enter the name of a month: ").lower()

if month == "february":
    days = "28 or 29 days"  
elif month in ("january", "march", "may", "july", "august", "october", "december"):
    days = "31 days"
elif month in ("april", "june", "september", "november"):
    days = "30 days"
else:
    days = "Invalid month name."

print(f"Number of days in {month}: {days}")