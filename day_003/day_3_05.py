#  Exercise 20:Ideal Gas Law
#  (19 Lines)
#  The ideal gas law is a mathematical approximation of the behavior of gasses as
#  pressure, volume and temperature change. It is usually stated as:
#  PV =nRT
#  where P is the pressure in Pascals, V is the volume in liters, n is the amount of
#  substance in moles, R is the ideal gas constant, equal to 8.314 J
#  mol K, and T is the
#  temperature in degrees Kelvin.
#  Write a programthat computes the amount of gas in moleswhentheusersupplies
#  the pressure, volume andtemperature. Test yourprogrambydeterminingthenumber
#  of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
#  a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
#  approximately 20 degrees Celsius or 68 degrees Fahrenheit
#  Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
#  to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
#  multiply it by 5
#  9 and then add 273.15 to it

R = 8.314

pressure = float(input("Enter the pressure (in Pascals): "))
volume = float(input("Enter the volume (in liters): "))
temperature_type = input("Enter the temperature type (C for Celsius, F for Fahrenheit): ").strip().upper()

if temperature_type == "C":
    temperature = float(input("Enter the temperature (in Celsius): ")) + 273.15
elif temperature_type == "F":
    temperature = (float(input("Enter the temperature (in Fahrenheit): ")) - 32) * 5 / 9 + 273.15
else:
    print("Invalid temperature type. Please enter C or F.")
    exit()

moles = (pressure * volume) / (R * temperature)

print(f"The amount of gas in moles is: {moles:.3f}")
