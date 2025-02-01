# Exercise 34:Even orOdd?
#  (Solved—13 Lines)
#  Write a program that reads an integer from the user. Then your program should
#  display a message indicating whether the integer is even or odd

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
