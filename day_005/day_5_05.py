# Exercise 35:DogYears
#  (22 Lines)
#  It is commonly said that one human year is equivalent to 7 dog years. However this
#  simple conversion fails to recognize that dogs reach adulthood in approximately two
#  years. As a result, some people believe that it is better to count each of the first two
#  human years as 10.5 dog years, and then count each additional human year as 4 dog
#  years.
human_years = int(input("Enter a human year: "))
if human_years <= 0:
    print("Invalid input. Human years must be positive.")
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

print(f"The dog age is {dog_years} dog years.")