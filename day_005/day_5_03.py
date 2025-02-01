# Exercise 33:Day OldBread
#  (Solved—19 Lines)
#  A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
#  percent. Write a program that begins by reading the number of loaves of day old
#  bread being purchased from the user. Then your program should display the regular
#  price for the bread, the discount because it is a day old, and the total price. All of the
#  values should be displayed using two decimal places, and the decimal points in all
#  of the numbers should be aligned when reasonable values are entered by the user

regular_price = 3.49
num_loaves = int(input("Enter the number of day-old loaves: "))
total_regular_price = regular_price * num_loaves
discount = total_regular_price * 0.60
total_price = total_regular_price - discount
print("Regular Price: ${:6.2f}".format(total_regular_price))
print("Discount:      ${:6.2f}".format(discount))
print("Total Price:   ${:6.2f}".format(total_price))