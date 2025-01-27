#  Manypeoplethinkabouttheirheightinfeetandinches,eveninsomecountriesthat
#  primarilyusethemetricsystem.Writeaprogramthatreadsanumberoffeetfrom
#  theuser,followedbyanumberofinches.Oncethesevaluesareread,yourprogram
#  shouldcomputeanddisplaytheequivalentnumberofcentimeters.
#  Hint:Onefootis12inches.Oneinchis2.54centimeters

feet = int(input("Enter your height in feet: "))
inches = int(input("Enter the remaining height in inches: "))


ipf = 12
cpi = 2.54


total_inches = (feet * ipf) + inches


total_cm = total_inches * cpi


print(f"Your height in centimeters is: {total_cm:.2f} cm")
