# Exercise 31:SumoftheDigitsinanInteger
#  (18 Lines)
#  Develop a program that reads a four-digit integer from the user and displays the sum
#  of the digits in the number. For example, if the user enters 3141 then your program
#   should display 3+1+4+1=9

num_str = input("Enter a four-digit integer: ")

if not num_str.isdigit() or len(num_str) != 4:
    print("Invalid input. Please enter a four-digit integer.")
    exit() 
digit1 = int(num_str[0])
digit2 = int(num_str[1])
digit3 = int(num_str[2])
digit4 = int(num_str[3])

sum_of_digits = digit1 + digit2 + digit3 + digit4

print(f"{digit1}+{digit2}+{digit3}+{digit4}={sum_of_digits}")
