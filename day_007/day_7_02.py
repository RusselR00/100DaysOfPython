#  Exercise 42:FrequencyToNote
#  (Solved—40 Lines)
#  In the previous question you converted from note name to frequency. In this question
#  you will write a program that reverses that process. Begin by reading a frequency
#  from the user. If the frequency is within one Hertz of a value listed in the table in
#  the previous question then report the name of the note. Otherwise report that the
#  frequency does not correspond to a known note. In this exercise you only need to
#  consider the notes listed in the table. There is no need to consider notes from other
#  octaves
frequencies = {
    261.63: "C4",
    293.66: "D4",
    329.63: "E4",
    349.23: "F4",
    392.00: "G4",
    440.00: "A4",
    493.88: "B4",
}

try:
    frequency = float(input("Enter a frequency (Hz): "))
    found_note = False

    for stored_frequency, note_name in frequencies.items():
        if abs(frequency - stored_frequency) <= 1:  
            print(f"The frequency corresponds to note {note_name}.")
            found_note = True
            break

    if not found_note:
        print("The frequency does not correspond to a known note.")

except ValueError:
    print("Invalid input. Please enter a numeric frequency.")