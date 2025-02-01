# Exercise 36:Vowel orConsonant
#  (Solved—16 Lines)
#  In this exercise you will create a program that reads a letter of the alphabet from the
#  user. If the user enters a, e, i, o or u then your program should display a message
#  indicating that the entered letter is a vowel. If the user enters y then your program
#  should display a message indicating that sometimes y is a vowel, and sometimes y is
#  a consonant. Otherwise your program should display a message indicating that the
#  letter is a consonant

letter = input("Enter a letter from the alphabet: ").lower()  

if letter in "aeiou":
    print(f"{letter} is a vowel.")
elif letter == "y":
    print(f"{letter} is sometimes a vowel and sometimes a consonant.")
elif letter.isalpha() and len(letter) == 1: 
    print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a single letter from the alphabet.")
