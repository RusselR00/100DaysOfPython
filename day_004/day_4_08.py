import math


air_temperature = float(input("Enter air temperature in degrees Celsius: "))
wind_speed = float(input("Enter wind speed in kilometers per hour: "))
if air_temperature > 10 or wind_speed <= 4.8:
    print("Wind chill index is not valid for these conditions.")
else:
    wind_chill_index = 13.12 + 0.6215 * air_temperature - 11.37 * math.pow(wind_speed, 0.16) + 0.3965 * air_temperature * math.pow(wind_speed, 0.16)

    print(f"Wind chill index: {round(wind_chill_index)}")