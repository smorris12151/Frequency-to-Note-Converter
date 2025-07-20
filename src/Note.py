import math
from NoteFactory import NoteFactory

class Note:
    #NOTE: noteFactory is an instance of NoteFactory class, with user defined AnchorA frequency, NOT the class itself
    def __init__(self, freq, factory):
        self.noteFactory = factory
        self.freq = freq
        self.name = factory.calculateNoteName(freq)
        self.octave = math.floor(factory.calculateOctave(freq))
        self.semitone = math.floor(factory.calculateSemitone(freq))
        self.cent = factory.calculateCents(freq)


    def getNoteFactory(self):
        return self.noteFactory    
    def __str__(self):
        return f"Note Name: {self.name}{self.octave}\nSemitones: {self.semitone}\nCents: {self.cent} "
        
    def calculateOverTones(self, numOverTones):
        
        overTones = []
        for i in range(1, numOverTones + 1):
            overToneFreq = self.freq * i
            overToneNote = Note(overToneFreq, self.getNoteFactory())
            overTones.append(overToneNote)
        return overTones
