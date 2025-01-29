#Create a program that reads two integers, a and b, from the user. Your program should
#compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of ab


from math import log10

while True:
    a = int(input("Enter an Integer"))
    b = int(input("Enter another integer"))
    if a>0 and b>0:
        sum = a+b
        diff = b-a
        product= a*b
        quotient = a%b
        reminder = a//b
        tentothelog = log10(a)
        power = a**b
        print('''The sum of a and b = %a \nThe difference when b is subtracted from a = %a\nThe product of a and b = %a \nThe quotient when a is divided by b = %a\nThe remainder when a is divided by b = %a \nThe result of log to the power 10 of a = %a \nThe result of ato the power b = %a''' % (sum,diff,product,quotient,reminder,tentothelog,power))

        break
    else:
        print("try again with 'integers'")
        continue

