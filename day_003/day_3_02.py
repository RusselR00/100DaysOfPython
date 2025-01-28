#  Exercise 17:Heat Capacity
#  (Solved—25 Lines)
#  Theamountofenergy required to increase the temperature of one gram of a material
#  by one degree Celsius is the material’s specific heat capacity, C. The total amount
#  of energy required to raise m grams of a material by ∆T degrees Celsius can be
#  computed using the formula:
#  q =mC∆T.
#  Write a program that reads the mass of some water and the temperature change
#  from the user. Your program should display the total amount of energy that must be
#  added or removed to achieve the desired temperature change.
#  Hint: Thespecificheatcapacityofwateris4.186 J
#  g◦C. Becausewaterhasaden
# sity of1.0grampermillilitre,youcanusegramsandmillilitresinterchangeably
#  in this exercise.
#  Extend your program so that it also computes the cost of heating the water. Elec
# tricity is normally billed using units of kilowatt hours rather than Joules. In this
#  exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
#  your program to compute the cost of boiling water for a cup of coffee
#  Hint: You will need to look up the factor for converting between Joules and
#  kilowatt hours to complete the last part of this exercise


mass = float(input("Enter the mass of water in grams (or milliliters): "))
temperature_change = float(input("Enter the temperature change in degrees Celsius: "))

SPECIFIC_HEAT_CAPACITY = 4.186 
JOULES_TO_KWH = 3.6e6  
ELECTRICITY_COST_PER_KWH = 8.9 / 100  

energy_required = mass * SPECIFIC_HEAT_CAPACITY * temperature_change  
print(f"\nThe total energy required is {energy_required:.2f} Joules.")


energy_in_kwh = energy_required / JOULES_TO_KWH
print(f"The energy required in kilowatt-hours is {energy_in_kwh:.6f} kWh.")


heating_cost = energy_in_kwh * ELECTRICITY_COST_PER_KWH
print(f"The cost of heating the water is ${heating_cost:.4f}.")
