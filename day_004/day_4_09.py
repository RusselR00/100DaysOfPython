#  Exercise 29:Celsius to Fahrenheit and Kelvin
#  (17 Lines)
#  Write a program that begins by reading a temperature from the user in degrees
#  Celsius. Then your program should display the equivalent temperature in degrees
#  Fahrenheit and degrees Kelvin. The calculations needed to convert between different
#  units of temperature can be found on the internet

celsius = float(input("Enter temperature in degrees Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperature in Kelvin: {kelvin:.2f} K")