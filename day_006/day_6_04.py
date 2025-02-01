#  Exercise 39:SoundLevels
#  (30 Lines)
#  The following table lists the sound level in decibels for several common noises.
#  Noise Decibellevel(dB)
#  Jackhammer 130
#  Gas lawnmower 106
#  Alarm clock 70
#  Quiet room 40
#  Write a program that reads a sound level in decibels from the user. If the user
#  enters a decibel level that matches one of the noises in the table then your program
#  should display a message containing only that noise. If the user enters a number
#  of decibels between the noises listed then your program should display a message
#  indicating whichnoisesthelevelisbetween.Ensurethatyourprogramalsogenerates
#  reasonable output for a value smaller than the quietest noise in the table, and for a
#  value larger than the loudest noise in the table

decibels = int(input("Enter a sound level in decibels: "))


if decibels == 130:
    print("Jackhammer")
elif decibels > 106:
    print("Between Jackhammer and Gas lawnmower")
elif decibels == 106:
    print("Gas lawnmower")
elif decibels > 70:
    print("Between Gas lawnmower and Alarm clock")
elif decibels == 70:
    print("Alarm clock")
elif decibels > 40:
    print("Between Alarm clock and Quiet room")
elif decibels == 40:
    print("Quiet room")
elif decibels > 0: 
    print("Quieter than a Quiet room")
elif decibels == 0:
    print("Absolute silence")
else: 
    print("Invalid decibel level. Decibels cannot be negative.")
