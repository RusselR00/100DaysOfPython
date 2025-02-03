#  Exercise44:DatetoHolidayName
#  (18Lines)
#  Canadahasthreenationalholidayswhichfallonthesamedateseachyear.
#  Holiday Date
#  Newyear’sday January1
#  Canadaday July1
#  Christmasday December25
#  Writeaprogramthatreadsamonthanddayfromtheuser.Ifthemonthandday
#  matchoneof theholidayslistedpreviouslythenyourprogramshoulddisplaythe
#  holiday’sname.Otherwiseyourprogramshouldindicatethattheenteredmonthand
#  daydonotcorrespondtoafixed-dateholiday.
#  Canadahastwoadditionalnationalholidays,GoodFridayandLabourDay,
#  whosedatesvaryfromyeartoyear.Therearealsonumerousprovincialand
#  territorialholidays,someofwhichhavefixeddates,andsomeofwhichhave
#  variabledates.Wewillnotconsideranyof theseadditionalholidaysinthis
#  exercise.
#  This
holidays = {
    "January 1": "New Year's Day",
    "July 1": "Canada Day",
    "December 25": "Christmas Day",
}

try:
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    date = f"{month} {day}"  # Create the combined date string

    if date in holidays:
        print(f"That date is {holidays[date]}.")
    else:
        print("That date does not correspond to a fixed-date holiday in Canada.")

except ValueError:  # Although unlikely with string input, good practice to include
    print("Invalid input.")  # More informative error message
