#  In the United States, fuel efficiency for vehicles is normally expressed in miles-per
# gallon (MPG). In Canada,fuel efficiency is normally expressed in liters-per-hundred
#  kilometers (L/100km). Use your research skills to determine how to convert from
#  MPGtoL/100km.ThencreateaprogramthatreadsavaluefromtheuserinAmerican
#  units and displays the equivalent fuel efficiency in Canadian units

mpg = float(input("Enter the fuel efficiency in Miles per Gallon:"))

lphk = 235.214/mpg

print('''Fuel efficiency of %a    Miles per Gallon in liters-per-hundred kilometers %a L/100km''' % (mpg,lphk))