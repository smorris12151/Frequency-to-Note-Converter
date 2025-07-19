import math
from NoteFactory import NoteFactory

class Note:
    #NOTE: noteFactory is an instance of NoteFactory class, with user defined AnchorA frequency, NOT the class itself
    def __init__(self, freq, noteFactory):
        self.noteFactory = noteFactory
        self.freq = freq
        self.name = noteFactory.calculateNoteName(freq)
        self.octave = math.floor(noteFactory.calculateOctave(freq))
        self.semitone = math.floor(noteFactory.calculateSemitone(freq))
        self.cent = noteFactory.calculateCents(freq)


    def getNoteFactory(self):
        return self.noteFactory    
    def __str__(self):
        return f"Note Name: {self.name}{self.octave}\nSemitones: {self.semitone}\nCents: {self.cent} "
        
    def calculateOverTones(self, numOverTones, verbosity = 0):
        
        overTones = []
        for i in range(1, numOverTones + 1):
            overToneFreq = self.freq * i
            overToneNote = Note(overToneFreq, self.getNoteFactory())
            overTones.append(overToneNote)
        if verbosity:
            for i in range(len(overTones)):
                if i == 0:
                    print("Root Note = " + str(overTones[i]) + " @ " + str(overTones[i].freq) + "Hz.")
                else:
                    print("Overtone " + str(i) + " = " + str(overTones[i]) + " @ " + str(overTones[i].freq) + "Hz.")
        return overTones
