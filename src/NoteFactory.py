import math
'''
NoteFactory class to define construction methods for Note objects
Octave attributor constructor dependant on anchorA value
All other attribute constructors dependant on octave method

'''
class NoteFactory:
    def __init__(self, anchorA):
        self.anchorA = anchorA
        self.C0 = round(anchorA * (2**(-57/12)), 2)
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
            'G#'
           ]
    def getAnchorA(self):
        return self.anchorA
    def getNoteNames(self):
        return self.noteNames
    def getC0(self):
        return self.C0
    def calculateOctave(self, inputFreq):
        # Returns a float for later calculations
        #NOTE Floor() this for printout in note class NOTE
        return math.log2(inputFreq/self.getC0())

    def calculateSemitone(self, inputFreq):
        #rounding semitone to 2 decimal places for simplicity of cent calculation.
        # NOTE if finding precision error later, try removing the round function here!! NOTE
        # NOTE Floor this for printout in note class NOTE
        return round((self.calculateOctave(inputFreq) * 12), 2) - 9
    
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
