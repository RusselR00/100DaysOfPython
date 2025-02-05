# Exercise 46:Season fromMonthandDay

# (Solved—40 Lines)

# The year is divided into four seasons: spring, summer, fall and winter. While the

# exact dates that the seasons change vary a little bit from year to year because of the

# waythatthecalendar is constructed, we will use the following dates for this exercise:

# Season Firstday

# Spring March20

# Summer June21

# Fall September22

# Winter December21

# Create a program that reads a month and day from the user. The user will enter

# the name of the month as a string, followed by the day within the month as an

# integer. Then your program should display the season associated with the date that

# was entered
month = input("Enter the month: ")
day = int(input("Enter the day: "))

if month == "March":
    if day >= 20:
        season = "Spring"
    else:
        season = "Winter"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day >= 21:
        season = "Summer"
    else:
        season = "Spring"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "September":
    if day >= 22:
        season = "Fall"
    else:
        season = "Summer"
elif month == "October" or month == "November":
    season = "Fall"
elif month == "December":
    if day >= 21:
        season = "Winter"
    else:
        season = "Fall"
elif month == "January" or month == "February":
    season = "Winter"
else:
    print("Invalid month entered.")
    exit()


print("The season is:", season)