# Exercise 30:Units of Pressure
#  (20 Lines)
#  In this exercise you will create a program that reads a pressure from the user in kilo
# pascals. Once the pressure has been read your program should report the equivalent
#  pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
#  your research skills to determine the conversion factors between these units

pressure_kpa = float(input("Enter pressure in kilopascals (kPa): "))

kpa_to_psi = 0.145038 
kpa_to_mmHg = 7.50062 
kpa_to_atm = 0.00986923  
pressure_psi = pressure_kpa * kpa_to_psi
pressure_mmHg = pressure_kpa * kpa_to_mmHg
pressure_atm = pressure_kpa * kpa_to_atm

print(f"Pressure in pounds per square inch (psi): {pressure_psi:.2f}")
print(f"Pressure in millimeters of mercury (mmHg): {pressure_mmHg:.2f}")
print(f"Pressure in atmospheres (atm): {pressure_atm:.2f}")