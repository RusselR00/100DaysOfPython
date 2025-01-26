# Inmanyjurisdictionsasmalldepositisaddedtodrinkcontain
# erstoencouragepeople to recycle them. In one 
# particular jurisdiction, drink containers holding 
# one liter or less have a $0.10 deposit, and drink 
# containers holding more than one liter have a $0.25 
# deposit. Write a program that reads the number of 
# containers of each size from the user. Your program 
# should continue by computing and displaying the 
# refund that will be received for returning those 
# containers. Format the output so that it includes a
#  dollar sign and always displays exactly two 
# decimal places.

a = float(input("number of drinking containers holding 1 liter or less"))
b = float(input("number of drinking containers holding more than 1 liter "))
c= (a*0.10+b*0.25)

print("Refund for returing the containers is $ %.2f" % c)