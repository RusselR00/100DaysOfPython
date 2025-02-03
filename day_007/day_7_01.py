#  Exercise 41:NoteToFrequency
#  (Solved—39 Lines)
#  The following table lists an octave of music notes, beginning with middle C, along
#  with their frequencies.
#  Note Frequency(Hz)
#  C4 261.63
#  D4 293.66
#  E4 329.63
#  F4 349.23
#  G4 392.00
#  A4 440.00
#  B4 493.88
# Begin by writing a program that reads the name of a note from the user and
#  displays the note’s frequency. Your program should support all of the notes listed
#  previously.
#  Onceyouhaveyourprogramworkingcorrectlyforthenoteslistedpreviouslyyou
#  should add support for all of the notes from C0 to C8. While this could be done by
#  adding many additional cases to your if statement, such a solution is cumbersome,
#  inelegant and unacceptable for the purposes of this exercise. Instead, you should
#  exploittherelationshipbetweennotesinadjacentoctaves.Inparticular,thefrequency
#  of anynoteinoctaven ishalfthefrequencyofthecorrespondingnoteinoctaven+1.
#  Byusing this relationship, you should be able to add support for the additional notes
#  without adding additional cases to your if statement.
#  Hint: To complete this exercise you will need to extract individual characters
#  from the two-character note name so that you can work with the letter and
#  the octave number separately. Once you have separated the parts, compute the
#  frequency of the note in the fourth octave using the data in the table above.
#  Then divide the frequency by 24−x, where x is the octave number entered by
#  the user. This will halve or double the frequency the correct number of times

frequencies = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88,
}

try:
    note_name = input("Enter a note name (e.g., C4, A0, G8): ")
    note = note_name[0].upper()
    octave = int(note_name[1])

    if note not in frequencies:
        print("Invalid note name.")
    else:
        base_frequency = frequencies[note]

        if octave < 4:
            frequency = base_frequency / (2**(4 - octave))
        elif octave > 4:
            frequency = base_frequency * (2**(octave - 4))
        else:
            frequency = base_frequency

        print(f"The frequency of {note_name} is {frequency:.2f} Hz.")

except (ValueError, IndexError):
    print("Invalid note name.")