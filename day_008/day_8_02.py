# Exercise 47:Birth Date to Astrological Sign

# (47 Lines)

# The horoscopes commonly reported in newspapers use the position of the sun at the

# time of one’s birth to try and predict the future. This system of astrology divides the

# year into twelve zodiac signs, as outline in the table below:

# Zodiac sign Daterange

# Capricorn December22toJanuary19

# Aquarius January20toFebruary18

# Pisces February19toMarch20

# Aries March21toApril19

# Taurus April20toMay20

# Gemini May21toJune20

# Cancer June21toJuly22

# Leo July23toAugust22

# Virgo August23toSeptember22

# Libra September23toOctober22

# Scorpio October23toNovember21

# Sagittarius November22toDecember21

# Write a programthat asks the user to enter his or her month and day of birth. Then

# your program should report the user’s zodiac sign as part of an appropriate output

# message.

month = input("Enter your birth month: ")
day = int(input("Enter your birth day: "))

if month == "January":
    if day <= 19:
        sign = "Capricorn"
    else:
        sign = "Aquarius"
elif month == "February":
    if day <= 18:
        sign = "Aquarius"
    else:
        sign = "Pisces"
elif month == "March":
    if day <= 20:
        sign = "Pisces"
    else:
        sign = "Aries"
elif month == "April":
    if day <= 19:
        sign = "Aries"
    else:
        sign = "Taurus"
elif month == "May":
    if day <= 20:
        sign = "Taurus"
    else:
        sign = "Gemini"
elif month == "June":
    if day <= 20:
        sign = "Gemini"
    else:
        sign = "Cancer"
elif month == "July":
    if day <= 22:
        sign = "Cancer"
    else:
        sign = "Leo"
elif month == "August":
    if day <= 22:
        sign = "Leo"
    else:
        sign = "Virgo"
elif month == "September":
    if day <= 22:
        sign = "Virgo"
    else:
        sign = "Libra"
elif month == "October":
    if day <= 22:
        sign = "Libra"
    else:
        sign = "Scorpio"
elif month == "November":
    if day <= 21:
        sign = "Scorpio"
    else:
        sign = "Sagittarius"
elif month == "December":
    if day <= 21:
        sign = "Sagittarius"
    else:
        sign = "Capricorn"
else:
    print("Invalid month entered.")
    exit()

print("Your zodiac sign is:", sign)