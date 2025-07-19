'''
Main function from which we print greeting(s) and prompt user for input via argparse
'''
from Note import Note
from NoteFactory import NoteFactory

'''
Anchor frequency to base out notes around (consider this like the focal point of tuning a piano, based on frequency of A4)

'''
anchorA = float(input("Welcome, please input a value for your anchor frequency (default = A4 @ 440Hz) \n"))

noteFactory = NoteFactory(anchorA)
looper = "y"
while(looper == "y"):
    inputFreq = float(input("Please input a frequency to analyse: \n"))
    myNote = Note(inputFreq, noteFactory)
    numOvertones = int(input("How many overtones would you like?\n"))
    overTones = myNote.calculateOverTones(numOvertones)
    for i in range(len(overTones)):
                if i == 0:
                    print("Root Note = " + str(overTones[i]) + " @ " + str(overTones[i].freq) + "Hz.")
                else:
                    print("Overtone " + str(i) + " = " + str(overTones[i]) + " @ " + str(overTones[i].freq) + "Hz.")
    looper = input("\nWant to analyse another note?\ny/n\n")
