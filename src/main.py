'''
Main function from which we print greeting(s) and prompt user for input via argparse
'''
from Note import Note
from NoteFactory import NoteFactory

'''
Anchor frequency to base out notes around (consider this like the focal point of tuning a piano, based on frequency of A4)

'''
anchorA = float(input("Welcome, please input a value for your anchor frequency (default = A4 @ 440Hz) \n") or 440)

noteFactory = NoteFactory(anchorA)
looper = "y"
while(looper == "y"):
    inputFreq = float(input("Please input a frequency to analyse: \n"))
    myNote = Note(inputFreq, noteFactory)
    print("\nThe note at " + str(inputFreq) + "Hz is:")
    print(myNote)
    numOvertones = int(input("How many harmonics in your harmonic series?\n"))
    overTones = myNote.calculateOverTones(numOvertones)
    for i in range(numOvertones):
                if i == 0:
                    print("\n***Root Note***\n" + str(overTones[i]) + "\nFrequency:  " + str(overTones[i].freq) + "Hz.")
                else:
                    print("\n***Overtone " + str(i) + "***\n" + str(overTones[i]) + "\nFrequency: " + str(overTones[i].freq) + "Hz.")
    looper = input("\nWant to analyse another note?\ny/n\n")
