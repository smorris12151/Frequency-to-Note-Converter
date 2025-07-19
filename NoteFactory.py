import math
'''
NoteFactory class to define construction methods for Note objects
Octave attributor constructor dependant on anchorA value
All other attribute constructors dependant on octave method

'''
class NoteFactory:
    def __init__(self, anchorA):
        self.anchorA = anchorA
        self.baseFreqs = {
            'C': 16.35,
            'C#': 17.32,
            'D': 18.35,
            'D#': 19.45,
            'E': 20.6,
            'F': 21.83,
            'F#': 23.12,
            'G': 24.5,
            'G#': 25.96,
            'A': 27.5,
            'A#': 29.14,
            'B': 30.87
            }
        self.noteNames = [
            'A',
            'A#',
            'B',
            'C',
            'C#',
            'D',
            'D#',
            'E',
            'F',
            'F#',
            'G',
            'G#']
    def getAnchorA(self):
        return self.anchorA
    def getNoteNames(self):
        return self.noteNames
    def calculateOctave(self, inputFreq):
        # Returns a float for later calculations
        #NOTE Floor() this for printout in note class NOTE
        return math.log2(inputFreq/self.getAnchorA()) + 4

    def calculateSemitone(self, inputFreq):
        #rounding semitone to 2 decimal places for simplicity of cent calculation.
        # NOTE if finding precision error later, try removing the round function here!! NOTE
        # NOTE Floor this for printout in note class NOTE
        return round((self.calculateOctave(inputFreq) * 12), 2)
    
    def calculateCents(self, inputFreq):
        # mod 1 takes the digits behind the decimal, multiply by 10 for int value of cents
        # NOTE written to work with rounded semitone calculation; may need to be modified for precision later NOTE
        cents = self.calculateSemitone(inputFreq) % 1
        return int(cents*10)

    def calculateJump(self, inputFreq):
        #Returns integer jump from anchorA for referencing noteNames array
        return int(self.calculateSemitone(inputFreq) % 12)
    
    def calculateNoteName(self, inputFreq):
        index = self.calculateJump(inputFreq)
        return (self.getNoteNames())[index]
