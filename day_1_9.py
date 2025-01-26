#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.

deposit = float(input("Amount to be deposited to your savings account"))
afteryrOne= deposit+(deposit*.04)
afteryrTwo= afteryrOne+(afteryrOne*0.04)
afteryrThree=afteryrTwo+(afteryrTwo*0.04)

print(''' Amount at the Time of Withdrawl \nAfterOne Year %.2f\nAfter Two Years %.2f \nAfter Three Years %.2f'''% (afteryrOne,afteryrTwo,afteryrThree))